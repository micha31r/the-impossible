from django.db import models
from django.utils import timezone
from django.conf import settings

from usermgmt.models import (
	Profile,
)

User = settings.AUTH_USER_MODEL

class Idea(models.Model):

	# Order data by name
	class Meta:
		ordering = ['name']

	author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
	name = models.CharField(max_length=80,blank=False,unique=False)
	short_description = models.TextField(max_length=150,blank=False,unique=False)
	full_description = models.TextField(max_length=2000,blank=False,unique=False)
	viewed_user = models.ManyToManyField(Profile, related_name="viewed", blank=True)
	liked_user = models.ManyToManyField(Profile, related_name="liked", blank=True)
	timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now
	last_edit = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
