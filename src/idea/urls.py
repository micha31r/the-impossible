from django.urls import path

from .views import (
	explore_page,
	detail_page,
)

urlpatterns = [
	path('explore/<int:week_num>/<int:page_num>/', explore_page, name="explore_page"),
	path('detail/<int:pk>/', detail_page, name="detail_page"),
]
