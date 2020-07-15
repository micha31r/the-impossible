from django.db import models
from django.utils import timezone

FREQUENCY_OPTION = (
	(1,"Never"),
    (2,"Weekly"),
    (3,"Monthly"),
)

class Subscriber(models.Model):

	email = models.EmailField(max_length=250)
	frequency = models.IntegerField(default=1,choices=FREQUENCY_OPTION)

	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True)
	last_sent = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.email


