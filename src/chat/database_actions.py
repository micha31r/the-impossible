# Functions to interact with the database
# All functions must be asynchronous
from channels.db import database_sync_to_async

from .models import (
	ChatGroup,
	ChatPermission,
	ChatMessage,
)

@database_sync_to_async
# Check if user has access to this chat group
def user_in_chat_group(user, chat_group_slug):
	group = ChatGroup.objects.filter(slug=chat_group_slug).first()
	if group and group.member.filter(username=user.username).exists():
		permission = ChatPermission.objects.filter(user=user, group=group).first()
		if permission and permission.permitted:
			return True
	return False

# Save posted message to the database
@database_sync_to_async
def save_message(user, message, chat_group_slug):
	group = ChatGroup.objects.filter(slug=chat_group_slug).first()
	if group and len(message.replace(" ","")) > 0:
		obj = ChatMessage.objects.create(user=user, message=message[:1000])
		obj.save()

		group.message.add(obj)
		group.save()

