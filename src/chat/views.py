from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime, random

from the_impossible.utils import *

from the_impossible.ERROR import *

from usermgmt.models import Profile

from .models import (
	ChatGroup,
	ChatPermission,
	ChatMessage,
)

MESSAGE_PER_PAGE = 30

@login_required
def join_page(request):
	ctx = {}
	ctx["date"] = Date()

	template_file = "chat/join.html"
	return render(request,template_file,ctx)

@login_required
def chat_page(request,group):
	ctx = {}
	ctx["date"] = Date()

	group = get_object_or_404(ChatGroup, pk=pk)
	permission = get_object_or_404(ChatPermission, group=group)

	# Requesting user must be a verified member from this group
	if not group.member.filter(username=username).exists() or not permission.permitted:
		return redirect("access_error_page")

	# Only retrieve the most recent 20 messages, the rest will be loaded when necessary via AJAX
	ctx["recent_messages"] = recent_messages = ChatMessage.objects.filter(to_group=group).order_by("-timestamp")[:MESSAGE_PER_PAGE]

	template_file = "chat/app.html"
	return render(request,template_file,ctx)

# Below are AJAX views to send / receive / delete messages

@login_required
def add_message_view(request):
	pass

@login_required
def delete_message_view(request):
	pass

@login_required
def get_message_view(request):
	pass




