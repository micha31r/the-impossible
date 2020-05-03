from django.db import models
from django.utils import timezone
from django.conf import settings

from usermgmt.models import (
	Profile,
)

from userupload.models import (
	File,
	Link
)

User = settings.AUTH_USER_MODEL

PUBLISH_OPTION = (
	(1,"Private"),
    (2,"Public"),
    (3,"Followers only"),
)

class Tag(models.Model):
	class Meta:
		ordering = ['name']

	name = models.CharField(max_length=100, blank=False, unique=True)

	def __str__(self):
		return self.name


class Idea(models.Model):

	# Order data by name
	class Meta:
		ordering = ['name']

	# Settings
	author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
	publish_stats = models.IntegerField(default=1,choices=PUBLISH_OPTION)
	tags = models.ManyToManyField(Tag,related_name="tagged",blank=True)

    # Content
	header_img = models.ForeignKey(File,on_delete=models.SET_NULL,blank=True,null=True)
	body_img = models.ManyToManyField(File,related_name="body_image",blank=True)

	name = models.CharField(max_length=80,blank=False,unique=False)
	short_description = models.TextField(max_length=150,blank=False,unique=False)
	full_description = models.TextField(max_length=2000,blank=False,unique=False)
	
	# Likes and views
	viewed_user = models.ManyToManyField(Profile, related_name="viewed", blank=True)
	liked_user = models.ManyToManyField(Profile, related_name="liked", blank=True)
	
	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now
	last_edit = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
