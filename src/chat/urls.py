from django.urls import path

from . import views

app_name = "chat"

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('<str:chat_group_slug>', views.app_page, name='app_page'),
]