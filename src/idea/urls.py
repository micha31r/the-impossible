from django.urls import path

from .views import (
	explore_page,
	detail_page,
	create_view,
	edit_page,
	like_view,
)

urlpatterns = [
	path('explore/<int:week_num>/<int:page_num>/', explore_page, name="idea_explore_page"),
	path('detail/<int:pk>/', detail_page, name="idea_detail_page"),
	path('create/', create_view, name="idea_create_view"),
	path('edit/<int:pk>/', edit_page, name="idea_edit_page"),
	path('like/', like_view, name="idea_like_view"),
] 