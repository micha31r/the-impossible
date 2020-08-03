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

from .models import ChatGroup, ChatMessage

@login_required
def chat_page(request,to_username):
	my_profile = get_object_or_404(Profile,user=request.user)
	to_user = get_object_or_404(User,username=to_username,is_active=True)
	# if my_profile.followingfilter()
