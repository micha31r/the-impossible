from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime

from .utils import *

from .ajax_encrypt import encrypt

from .models import (
	Idea,
)

from usermgmt.models import (
	Profile,
)

from .forms import *

from the_impossible.ERROR import *

MINIMUM_DATE = datetime.datetime.date(datetime.datetime(2020, 4, 9))
ITEM_PER_PAGE = 12

def explore_page(request,week_num,page_num):
	ctx = {} # Context variables
	ctx["date"] = date = Date()
	ctx["week_num"] = week_num
	ctx["page_num"] = page_num
	today = date.now()
	# Note: current date is not the date, its year/week/1
	current_date = int_date(f"{today.strftime('%Y')}-{week_num}-1")
	ctx['from_date'] = timestamp_from = current_week_dates(*current_date)
	ctx['to_date'] = timestamp_to = timestamp_from + datetime.timedelta(days=7)
	# Check if previous and next week numbers are valid
	if timestamp_from > MINIMUM_DATE: ctx["previous_week_num"] = week_num - 1
	if week_num < current_week(): ctx["next_week_num"] = week_num + 1
	if request.user.is_authenticated: 
		ctx["profile"] = Profile.objects.filter(user=request.user).first()
		ctx["encrypted_string"] = encrypt(request.user.username)
	# Filter by date
	# https://stackoverflow.com/questions/4923612/filter-by-timestamp-in-query
	ideas = Idea.objects.filter(
		timestamp__gte = timestamp_from,
		timestamp__lt = timestamp_to,
	).distinct().reverse()
	# Split data into pages
	ideas = Paginator(ideas,ITEM_PER_PAGE)
	ctx["max_page"] = ideas.num_pages
	try: current_page = ideas.page(page_num) # Get the ideas on the current page
	except: raise Http404()
	ctx["ideas"] = current_page 
	template_file = "idea/explore.html"
	return render(request,template_file,ctx)

@login_required
def detail_page(request,pk):
	ctx = {} # Context variables
	ctx["date"] = Date()
	ctx["idea"] = idea = get_object_or_404(Idea, pk=pk)
	# Add view count
	ctx["profile"] = profile = get_object_or_404(Profile, user=request.user)
	idea.viewed_user.add(profile)
	ctx["encrypted_string"] = encrypt(request.user.username)
	template_file = "idea/detail.html"
	return render(request,template_file,ctx)

@login_required
def edit_page(request,pk):
	ctx = {} # Context variables
	ctx["date"] = Date()
	ctx["idea"] = idea = get_object_or_404(Idea, pk=pk)
	profile = Profile.objects.filter(user=request.user).first()
	if idea.author == profile:
		ctx["form"] = form = IdeaForm(request.POST or None)
		if form.is_valid():
			inputs = form.cleaned_data
			idea.name = inputs.get("name")
			idea.short_description = inputs.get("short_description")
			idea.full_description = inputs.get("full_description")
			idea.save()
			ctx["form"] = form = IdeaForm(request.POST or None)
		else:
			# Set default values for the form
			initial = {
				"name":idea.name,
				"short_description":idea.short_description,
				"full_description":idea.full_description,
			}
			ctx["form"] = form = IdeaForm(initial=initial)
	else:
		ctx["error"] = SERVER_ERROR["ACCESS"]
	template_file = "idea/edit.html"
	return render(request,template_file,ctx)

def like_view(request):
	data = {}
	try:
		# Check if request is send by the correct user
		if request.GET.get('encrypted_string') == encrypt(request.GET.get('username')) and request.is_ajax():
			# Get object pk
			pk = request.GET.get('pk', None)
			username = request.GET.get('username', None)
			# Retrieve objects
			idea = Idea.objects.filter(pk=pk).first()
			user = User.objects.filter(username=username).first()
			profile = Profile.objects.filter(user=user).first()
			# Add like
			if profile in idea.liked_user.all(): 	# -|
				data["action"] = "unliked"			# Unliked
				idea.liked_user.remove(profile) 	# -|
			else: 									# -|			
				idea.liked_user.add(profile)		# Liked
				data["action"] = "liked"			# -|
			data['updated_like_count'] = idea.liked_user.count()
		else:
			raise CustomError("AjaxInvalid")
	except:
		data['failed'] = True
	return JsonResponse(data)

