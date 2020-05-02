from django.shortcuts import render

from .utils import *

# Home page
def home_page(request):
	ctx = {}
	ctx["date"] = Date()
	template_file = "home.html"
	return render(request,template_file,ctx)
