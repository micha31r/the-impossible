from django.db import models
from usermgmt.models import Profile

class Feedback(models.Model):
	author = models.ForeignKey(
	    Profile,
	    on_delete=models.CASCADE,
	)
	short_description = models.CharField(max_length=150, blank=False)
	description = models.CharField(max_length=1000, blank=True)
	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) 

class Question(models.Model):
	author = models.ForeignKey(
	    Profile,
	    on_delete=models.CASCADE,
	)
	short_description = models.CharField(max_length=150, blank=False)
	description = models.CharField(max_length=1000, blank=True)
	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) 

class CoreFeed(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) 

