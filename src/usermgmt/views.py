from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import (
	LoginForm,
)

def login_page(request):
	ctx = {} # Context variables
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
			ctx["obj_error"] = f"User {OBJECT_ERROR[0]}"
	login_form = LoginForm()
	template_file = "usermgmt/login.html"
	return render(request,template_file,ctx)

def logout_view(request):
    logout(request)
    return redirect("login_page")

