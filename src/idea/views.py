from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

from .models import (
	Idea,
)

from usermgmt.models import (
	Profile,
)

MINIMUM_DATE = datetime.date(datetime(2020, 4, 9))
ITEM_PER_PAGE = 7

# Note: week_num starts at 0 while page_num starts at 1
def explore_page(request,week_num,page_num):
	ctx = {} # Context variables
	ctx["week_num"] = week_num
	ctx["page_num"] = page_num
	today = datetime.now().date()
	ctx['from_date'] = timestamp_from = datetime.now().date() - timedelta(days=(week_num+1)*7)
	ctx['to_date'] = timestamp_to = timestamp_from + timedelta(days=8)
	# Check if previous and next week numbers are valid
	if timestamp_from > MINIMUM_DATE: ctx["previous_week_num"] = week_num + 1
	if week_num >= 1: ctx["next_week_num"] = week_num - 1
	if True: # request.user.is_authenticated
		# Filter by date
		# https://stackoverflow.com/questions/4923612/filter-by-timestamp-in-query
		ideas = Idea.objects.filter(
			timestamp__gte = timestamp_from,
    		timestamp__lt = timestamp_to,
		).distinct()
		if ideas.count() > 1:
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
	ctx["idea"] = idea = get_object_or_404(Idea, pk=pk)
	template_file = "idea/detail.html"
	return render(request,template_file,ctx)

