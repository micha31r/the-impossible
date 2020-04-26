from django.urls import path

from .views import (
	explore_page,
	detail_page,
	create_view,
	edit_page,
	remove_tag_view,
	like_view,
)

urlpatterns = [
	path('explore/<int:week_num>/<int:page_num>/', explore_page, name="explore_page"),
	path('detail/<int:pk>/', detail_page, name="detail_page"),
	path('create/', create_view, name="create_view"),
	path('edit/<int:pk>/', edit_page, name="edit_page"),
	path('remove-tag/<int:pk>/<int:tag_pk>/', remove_tag_view, name="remove_tag_view"),
	path('like/', like_view, name="like_view"),
]
