from django.urls import path

from .views import (
	join_page,
	chat_page,
)

app_name = 'chat'

urlpatterns = [
	# Chat
	path('join', chat_page, name="join_page"),
	path('app/<slug:group_pk>', chat_page, name="chat_page"),
]