from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import (
	ChatGroup,
)

from the_impossible.utils import *

@login_required
def home_page(request):
	ctx = {}
	ctx["date"] = Date()
	user = request.user

	# Retrieve all chat groups that containers this user
	ctx["chat_groups"] = ChatGroup.objects.filter(member__id__exact=user.id)

	return render(request, 'chat/home.html', ctx)

@login_required
def app_page(request, chat_group_slug):
	ctx = {}
	ctx["date"] = Date()
	ctx["chat_group_slug"] = chat_group_slug

	group = get_object_or_404(ChatGroup,slug=chat_group_slug)

	# Get recent messages posted in this chat group
	ctx["recent_messages"] = group.message.order_by("timestamp")[:200]

	return render(request, 'chat/app.html', ctx)
