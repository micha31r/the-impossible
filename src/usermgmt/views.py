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

from .models import Profile

from userupload.models import File

from idea.ajax_encrypt import encrypt

from idea.models import Idea

from the_impossible.utils import *

from the_impossible.ERROR import *

ITEM_PER_PAGE = 20
NOTIFICATION_PER_PAGE = 50

def signup_page(request):
	ctx = {} # Context variables
	ctx["date"] = Date()
	next_page = request.GET.get("next") # Get url of the next page
	if request.user.is_authenticated:
		return redirect(next_page or "home_page")
	signup_form = SignUpForm(request.POST or None)
	ctx["signup_form"] = signup_form
	if signup_form.is_valid():
		# Get form inputs
		first_name = signup_form.cleaned_data.get("first_name")
		last_name = signup_form.cleaned_data.get("last_name")
		username = signup_form.cleaned_data.get("username")
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
						# Log user in
						login(request, user)
						return redirect(next_page or "home_page") # Redirect to the next page
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
		return redirect(next_page or "home_page")
	login_form = LoginForm(request.POST or None)
	ctx["login_form"] = login_form
	if login_form.is_valid():
		username = login_form.cleaned_data.get("username")
		password = login_form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect(next_page or "home_page") # Redirect to the next page
		else: 
			# Display error if user is not found
			ctx["error"] = SERVER_ERROR["AUTH_LOGIN"]
	login_form = LoginForm()
	template_file = "usermgmt/login.html"
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
	user = get_object_or_404(User, username=username)
	# The profile for the logged in user
	if request.user.is_authenticated:
		ctx["profile"] = Profile.objects.filter(user=request.user).first()
	ctx["encrypted_string"] = encrypt(request.user.username)
	# The profile for the viewed user
	ctx["target_profile"] = target_profile = get_object_or_404(Profile,user=user)
	# Get 20 most recent notifications
	ctx["target_notifications"] = target_profile.notification.all().order_by('-timestamp')[:20]
	
	# Followers
	ctx["followers"] = followers = User.objects.filter(profile__following=target_profile.user)
	ctx["followers_profile"] = []
	for follower in followers[:30]:
		ctx["followers_profile"].append(Profile.objects.filter(user=follower).first())

	ideas = {}
	if content_filter == "my":
		# Ideas created by this user
		ideas = Idea.objects.filter(author=target_profile).order_by("timestamp").reverse()[:20]
	elif content_filter == "liked":
		# Liked ideas 
		ideas = Idea.objects.filter(liked_user=target_profile)
	elif content_filter == "starred":
		if user == request.user: # Starred ideas are private
			# Starred ideas 
			ideas = Idea.objects.filter(starred_user=target_profile)[:5]
		else: raise Http404()
	else: raise Http404()

	# Split data into pages
	ideas = Paginator(ideas,ITEM_PER_PAGE)
	ctx["max_page"] = ideas.num_pages
	try: current_page = ideas.page(page_num) # Get the ideas on the current page
	except: raise Http404()
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
	notifications = Paginator(profile.notification.all().order_by("-timestamp"),NOTIFICATION_PER_PAGE)
	ctx["max_page"] = notifications.num_pages
	try: current_page = notifications.page(page_num) # Get the ideas on the current page
	except: raise Http404()
	ctx["notifications"] = current_page 
	template_file = "usermgmt/account_notification.html"
	return render(request,template_file,ctx)

@login_required
def account_follow_view(request,username):
	target_user = get_object_or_404(User,username=username)
	profile = get_object_or_404(Profile,user=request.user)
	if profile.following.filter(username=target_user.username).exists():
		profile.following.remove(target_user)
	else:
		profile.following.add(target_user)
	profile.save()
	return redirect("account_dashboard_page",username=username,content_filter="my",page_num=1)



