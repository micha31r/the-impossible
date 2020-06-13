from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import (
	LoginForm,
	SignUpForm,
)

from .models import (
	Profile,
)

from idea.models import (
	Idea
)

from the_impossible.utils import *

from the_impossible.ERROR import *

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
						# Create a profile
						profile = Profile.objects.create(
							user=user
						)
						# Log user in
						login(request, user)
						return redirect(next_page or "home_page") # Redirect to the next page
			else: ctx["error"] = SERVER_ERROR["SIGNUP_EMAIL_TAKEN"]
		else: ctx["error"] = SERVER_ERROR["SIGNUP_USERNAME_TAKEN"]
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
			ctx["error"] = SERVER_ERROR["LOGIN"]
	login_form = LoginForm()
	template_file = "usermgmt/login.html"
	return render(request,template_file,ctx)

@login_required
def logout_view(request):
    logout(request)
    return redirect("login_page")

@login_required
def account_dashboard_page(request):
	ctx = {}
	ctx["date"] = Date()
	ctx["profile"] = profile = get_object_or_404(Profile,user=request.user)
	ctx["liked_idea"] = liked_idea = Idea.objects.filter(liked_user=profile)[:5]
	ctx["starred_idea"] = starred_idea = Idea.objects.filter(starred_user=profile)[:5]
	# 5 Recently viewed ideas
	ctx["viewed_idea"] = viewed_idea = Idea.objects.filter(viewed_user=profile)[:10]
	print(liked_idea)

	template_file = "usermgmt/account_dashboard.html"
	return render(request,template_file,ctx)


