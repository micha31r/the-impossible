from django.urls import path

from .views import (
	chat_page,
)

app_name = 'chat'

urlpatterns = [
	# Chat
	path('app/<slug:to_username>', chat_page, name="chat_page"),
]