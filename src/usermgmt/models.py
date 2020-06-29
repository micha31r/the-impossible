from django.db import models
from django.conf import settings

from userupload.models import File

User = settings.AUTH_USER_MODEL

PUBLISH_OPTION = (
	(1,"Private"),
    (2,"Public"),
)

LIKE_OPTION = (
	(1,"Off"),
    (2,"From Followers"),
    (3,"From Everyone"),
)

COMMENT_OPTION = (
	(1,"No Comments"),
    (2,"From Followers"),
    (3,"From Everyone"),
)

DISCOVER_OPTION = (
	(1,"Hide"),
    (2,"Discoverable"),
)

class Notification(models.Model):
	message = models.CharField(max_length=200)
	message_status = models.IntegerField(default=1,choices=PUBLISH_OPTION)
	dismissed = models.BooleanField(default=False)
	link = models.URLField(max_length=200,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now

class Profile(models.Model):
	user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

	profile_img = models.ForeignKey(File,on_delete=models.SET_NULL,blank=True,null=True)
	bio = models.TextField(max_length=160,blank=True,unique=False)
	website = models.URLField(max_length=160,blank=True,unique=False)
	location = models.CharField(max_length=50,blank=True,null=True)
	following = models.ManyToManyField(User,blank=True,related_name="following")
	notification = models.ManyToManyField(Notification,blank=True,related_name="notification")
	tags = models.ManyToManyField("idea.Tag",blank=True,related_name="fav_tags")
	blocked_user = models.ManyToManyField(User,blank=True,related_name="blocked")
	
	# Social settings
	like_setting = models.IntegerField(default=1,choices=LIKE_OPTION)
	comment_setting = models.IntegerField(default=1,choices=COMMENT_OPTION)
	# Allow others to see this user in Discover People Page
	discover_setting = models.IntegerField(default=1,choices=DISCOVER_OPTION)

    # Only allow each user to post 5 ideas per day
	daily_limit = models.IntegerField(default=5)
	daily_limit_timestamp = models.DateTimeField(auto_now=True)

	timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now

	def __str__(self):
		full_name = "Anonymous"
		try: full_name = self.user.get_full_name() 
		except: pass
		return full_name 