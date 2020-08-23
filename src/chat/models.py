import string, random
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

def slug_generator(seed,size=20, chars=string.ascii_letters + string.digits):
	random.seed(seed)
	return ''.join(random.choice(chars) for _ in range(size))

class ChatMessage(models.Model):

	# Order data by name
	class Meta:
		ordering = ['-id']

	user = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		null=True
	)

	message = models.CharField(max_length=1000)

	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message

class ChatGroup(models.Model):

	# Order data by name
	class Meta:
		ordering = ['name']

	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)

	name = models.CharField(max_length=200)
	slug = models.SlugField(blank=True)
	key = models.SlugField(blank=True)

	# Each group can have a maximum of 500 members
	member = models.ManyToManyField(
		User,
		related_name="member",
		blank=True
	)

	# set related_name to "messages" so it doesn't conflict with ChatMessage.message
	message = models.ManyToManyField(
		ChatMessage,
		related_name="messages",
		blank=True
	)

	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) 

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if not self.slug:
			self.slug = slug_generator(self.id+len(self.name), size=10)
		if not self.key:
			self.key = slug_generator(self.id, size=6)
		super().save(*args, **kwargs)

	def add_member(self,user):
		# Requesting member(user) must be an active user
		if user.is_active:
			if self.member.count() < 500:
				self.member.add(user)
				self.save()
				return True
		return False

	# If this group has only 2 members than it's considered as direct messaging
	def is_direct(self):
		if self.member.all().count() == 2:
			return True
		return False

	def __str__(self):
		return self.name

# New users must be approved before added to a chat
class ChatPermission(models.Model):
	
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)

	permitted = models.BooleanField(default=False)
	group = models.ForeignKey(
		ChatGroup,
		related_name="group",
		on_delete=models.CASCADE
	)

	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) 

	def delete(self, *args, **kwargs):
		self.group.member.remove(self.user)
		super(Image, self).delete(*args, **kwargs)



