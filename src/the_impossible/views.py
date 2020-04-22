from django.shortcuts import render

from idea.utils import *

# Home page
def home_page(request):
	ctx = {}
	ctx["date"] = Date()
	template_file = "home.html"
	return render(request,template_file,ctx)
