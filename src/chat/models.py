from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ChatGroup(models.Model):

	# Order data by name
	class Meta:
		ordering = ['name']

	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)

	name = models.CharField(max_length=200)

	# Each group can have a maximum of 500 members
	member = models.ManyToManyField(
		User,
		related_name="member",
		blank=True
	)

	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) 

	def add_member(user):
		if self.member.count() < 500:
			self.member.add(user)
			self.save()
			return True
		return False

	def __str__(self):
		return self.name

class ChatMessage(models.Model):

	# Order data by name
	class Meta:
		ordering = ['-id']

	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)

	to_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name="to_user",
		blank=True,
	)

	to_group = models.ForeignKey(
		ChatGroup,
		on_delete=models.CASCADE,
		related_name="to_group",
		blank=True,
	)

	message = models.CharField(max_length=1000)

	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name



