from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django import forms

from .forms import (
	LoginForm,
	SignUpForm,
)

from .models import Profile, Notification

from userupload.models import File

from idea.models import Idea

from idea.utils import escape_html

from the_impossible.utils import *

from the_impossible.ERROR import *

IDEA_PER_PAGE = 20
NOTIFICATION_PER_PAGE = 50
USER_PER_PAGE = 20

def signup_page(request):
	ctx = {} # Context variables
	ctx["date"] = Date()
	next_page = request.GET.get("next") # Get url of the next page
	if request.user.is_authenticated:
		return redirect(next_page or "account_dashboard_page", username=request.user.username, content_filter="my", page_num=1) # Redirect to the next page
	signup_form = SignUpForm(request.POST or None)
	ctx["signup_form"] = signup_form
	if signup_form.is_valid():
		# Get form inputs
		first_name = signup_form.cleaned_data.get("first_name")
		last_name = signup_form.cleaned_data.get("last_name")
		username = escape_html(signup_form.cleaned_data.get("username")).replace(" ","_")
		email = signup_form.cleaned_data.get("email")
		password = signup_form.cleaned_data.get("password")
		password_confirmation = signup_form.cleaned_data.get("password_confirmation")
		# Make sure no user has the same username or email
		if not User.objects.filter(username=username).first():
			if not User.objects.filter(email=email).first():
				if password == password_confirmation: # Confirm password
					# Create user object
					user = User.objects.create_user(
						username=username,
						email=email,
						password=password
					)
					user.first_name = first_name.capitalize()
					user.last_name = last_name.capitalize()
					user.save()
					if user:
						# Profile image must have pk of 1 and created by superuser
						profile_img = File.objects.filter(id=1).first()
						if profile_img:
							if not profile_img.user.is_superuser:
								profile_img = None

						# Create a profile
						profile = Profile.objects.create(
							user=user,
							profile_img=profile_img or None
						)

						message = f"@{username}, welcome to The Impossible. If you have any questions, please contact us"
						msg = Notification.objects.create(message=message,message_status=1)
						msg.save()
						profile.notification.add(msg)

						# Log user in
						login(request, user)
						return redirect(next_page or "account_dashboard_page", username=user.username, content_filter="my", page_num=1) # Redirect to the next page
				else: ctx["error"] = SERVER_ERROR["AUTH_PASSWORD_MATCH"]
			else: ctx["error"] = SERVER_ERROR["AUTH_SIGNUP_EMAIL_TAKEN"]
		else: ctx["error"] = SERVER_ERROR["AUTH_SIGNUP_USERNAME_TAKEN"]
	signup_form = SignUpForm()
	template_file = "usermgmt/signup.html"
	return render(request,template_file,ctx)

def login_page(request):
	ctx = {} # Context variables
	ctx["date"] = Date()
	next_page = request.GET.get("next") # Get url of the next page
	if request.user.is_authenticated:
		return redirect(next_page or "account_dashboard_page", username=request.user.username, content_filter="my", page_num=1) # Redirect to the next page
	login_form = LoginForm(request.POST or None)
	ctx["login_form"] = login_form
	if login_form.is_valid():
		username = login_form.cleaned_data.get("username")
		password = login_form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect(next_page or "account_dashboard_page", username=user.username, content_filter="my", page_num=1) # Redirect to the next page
		else: 
			# Display error if user is not found
			ctx["error"] = SERVER_ERROR["AUTH_LOGIN"]
	login_form = LoginForm()
	template_file = "usermgmt/login.html"
	return render(request,template_file,ctx)

@login_required
def logout_page(request):
	ctx = {} # Context variables
	ctx["date"] = Date()
	template_file = "usermgmt/logout.html"
	return render(request,template_file,ctx)

@login_required
def logout_view(request):
    logout(request)
    return redirect("login_page")

def account_dashboard_page(request,username,content_filter,page_num):
	ctx = {}
	ctx["date"] = Date()
	ctx["page_num"] = page_num
	# Created ideas, liked ideas or starred ideas 
	ctx["content_filter"] = content_filter
	ctx["username"] = username
	user = get_object_or_404(User, username=username) # Target user
	# The profile for the logged in user
	if request.user.is_authenticated:
		ctx["profile"] = get_object_or_404(Profile,user=request.user)
	# The profile for the viewed user
	ctx["target_profile"] = target_profile = get_object_or_404(Profile,user=user)
	
	# Get 50 most recent notifications
	ctx["target_notifications"] = target_notifications = target_profile.notification.all().order_by('-pk')[:NOTIFICATION_PER_PAGE]
	# Check for unread notifications
	if request.user.is_authenticated and request.user == user:
		for msg in target_notifications:
			if not msg.dismissed:
				ctx["new_notification"] = True
	# Dismiss notifications
	ctx["undismissed_notifications"] = []
	if request.user == user:
		for notification in target_notifications:
			if not notification.dismissed:
				ctx["undismissed_notifications"].append(notification)
				notification.dismissed = True
				notification.save()

	# Get followers' profiles
	ctx["followers"] = followers = User.objects.filter(profile__following=target_profile.user)
	ctx["followers_profile"] = []
	for follower in followers[:30]:
		ctx["followers_profile"].append(Profile.objects.filter(user=follower).first())

	ideas = {}
	if content_filter == "my": # Ideas created by this user
		# Show all ideas is the current user is the same as the target user
		if request.user.is_authenticated and request.user == user:
			ideas = Idea.objects.filter(author=target_profile).order_by("timestamp").reverse()
		# If the current user follows the target user
		elif request.user.is_authenticated and ctx["profile"].following.filter(username=target_profile.user.username).exists():
			ideas = Idea.objects.filter(author=target_profile).exclude(publish_status=1).order_by("timestamp").reverse()
		else:
			ideas = Idea.objects.filter(author=target_profile, publish_status=3).order_by("timestamp").reverse()
	elif content_filter == "liked":
		# Blocked users can't see this page
		if target_profile.blocked_user.filter(username=request.user.username).exists():
			return redirect("access_error_page")
		# Liked ideas 
		ideas = Idea.objects.filter(liked_user=target_profile)
	elif content_filter == "starred":
		if user == request.user: # Starred ideas are private
			# Starred ideas 
			ideas = Idea.objects.filter(starred_user=target_profile)
		else: return redirect("access_error_page")
	else: raise Http404()

	# Split data into pages
	ideas = Paginator(ideas,IDEA_PER_PAGE)
	ctx["max_page"] = ideas.num_pages
	try: current_page = ideas.page(page_num) # Get the ideas on the current page
	except: raise Http404()
	# On the liked page, remove idea if the current user did not follow the idea's author
	# The filter is done here to optimise performance
	if content_filter == "liked" and user != request.user and request.user.is_authenticated:
		for idea in current_page:
			if not ctx["profile"].following.filter(username=idea.author.user.username).exists():
				current_page.object_list.remove(idea)
	ctx["masonary_ideas"] = current_page 
	template_file = "usermgmt/account_dashboard.html"
	return render(request,template_file,ctx)

@login_required
def account_notification_page(request,page_num):
	ctx = {}
	ctx["date"] = Date()
	ctx["page_num"] = page_num
	ctx["profile"] = profile = get_object_or_404(Profile,user=request.user)

	# Split data into pages
	notifications = Paginator(profile.notification.all().order_by("-pk"),NOTIFICATION_PER_PAGE)
	ctx["max_page"] = notifications.num_pages
	try: current_page = notifications.page(page_num) # Get the ideas on the current page
	except: raise Http404()
	ctx["notifications"] = current_page 

	# Check for new notifications
	for msg in current_page:
		if not msg.dismissed:
			ctx["new_notification"] = True
	# Dismiss notifications on this page
	ctx["undismissed_notifications"] = []
	for notification in current_page:
		if not notification.dismissed:
			ctx["undismissed_notifications"].append(notification)
			notification.dismissed = True
			notification.save()

	template_file = "usermgmt/account_notification.html"
	return render(request,template_file,ctx)

@login_required
def account_follow_view(request,username):
	target_profile = get_object_or_404(
		Profile,
		user=get_object_or_404(User,username=username)
	)
	profile = get_object_or_404(Profile,user=request.user)
	# Check if the current user is blocked by the target user
	if target_profile.blocked_user.filter(username=request.user.username).exists():
		message = f"@{username} blocked you, you cannot follow this user"
		msg = Notification.objects.create(message=message,message_status=1)
		msg.save()
		profile.notification.add(msg)
	else:
		# Check whether the current user is already following the target user
		if profile.following.filter(username=username).exists():
			profile.following.remove(target_profile.user)
		else:
			profile.following.add(target_profile.user)
	profile.save()
	return redirect("account_dashboard_page",username=username,content_filter="my",page_num=1)

@login_required
def account_people_page(request,username,follower_page_num,following_page_num):
	ctx = {}
	ctx["date"] = Date()
	ctx["profile"] = profile = get_object_or_404(Profile,user=request.user)

	# Blocked users can't see this page
	if request.user == profile.user or not profile.blocked_user.filter(username=request.user.username).exists():
		# Get followers
		followers = User.objects.filter(profile__following=request.user) # User obj
		followers = Profile.objects.filter(user__in=followers) # Profile obj	
		# Split data into pages
		followers = Paginator(followers,USER_PER_PAGE)
		ctx["follower_max_page"] = followers.num_pages
		try: current_page = followers.page(follower_page_num) # Get the ideas on the current page
		except: raise Http404()
		ctx["followers"] = current_page

		# Get following user
		# Split data into pages
		followings = Profile.objects.filter(user__in=profile.following.all())
		followings = Paginator(followings,USER_PER_PAGE)
		ctx["following_max_page"] = followings.num_pages
		try: current_page = followings.page(following_page_num) # Get the ideas on the current page
		except: raise Http404()
		ctx["followings"] = current_page  
	else:
		return redirect("access_error_page")

	template_file = "usermgmt/account_people.html"
	return render(request,template_file,ctx)

@login_required
def account_meet_page(request,username):
	ctx = {}
	ctx["date"] = Date()
	ctx["profile"] = profile = get_object_or_404(Profile,user=request.user)

	template_file = "usermgmt/account_meet.html"
	return render(request,template_file,ctx)





