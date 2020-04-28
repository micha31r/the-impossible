from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
	user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    # Only allow each user to post 5 ideas per day
	daily_limit = models.IntegerField(default=5)
	daily_limit_timestamp = models.DateTimeField(auto_now=True)

	timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now

	def __str__(self):
		full_name = "Anonymous"
		try: full_name = self.user.get_full_name() 
		except: pass
		return full_name 