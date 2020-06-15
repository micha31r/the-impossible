from django.db import models
from django.conf import settings

from userupload.models import File

User = settings.AUTH_USER_MODEL

PUBLISH_OPTION = (
	(1,"Private"),
    (2,"Public"),
    (3,"Dissmissed")
)

class Notification(models.Model):
	message = models.CharField(max_length=200)
	message_status = models.IntegerField(default=1,choices=PUBLISH_OPTION)
	link = models.URLField(max_length=200,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now

class Profile(models.Model):
	user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

	profile_img = models.ForeignKey(File,on_delete=models.SET_NULL,blank=True,null=True)
	bio = models.TextField(max_length=160,blank=True,unique=False)
	website = models.URLField(max_length=160,blank=True,unique=False)

	following = models.ManyToManyField(User, blank=True, related_name="following")

	notification = models.ManyToManyField(Notification, blank=True, related_name="notification")

    # Only allow each user to post 5 ideas per day
	daily_limit = models.IntegerField(default=5)
	daily_limit_timestamp = models.DateTimeField(auto_now=True)

	timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now

	def __str__(self):
		full_name = "Anonymous"
		try: full_name = self.user.get_full_name() 
		except: pass
		return full_name 