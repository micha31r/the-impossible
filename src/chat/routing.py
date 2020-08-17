# This is similar to urls.py, but for websocket connections

from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<slug:chat_group_slug>', consumers.ChatConsumer),
]