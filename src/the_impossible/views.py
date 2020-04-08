from django.shortcuts import render

# Home page
def home_page(request):
	ctx = {}
	template_file = "home.html"
	return render(request,template_file,ctx)
