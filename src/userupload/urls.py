from django.urls import path

from .views import (
	idea_img_page,
	delete_page
)

urlpatterns = [
	path('file/idea/header/<int:idea_pk>/<slug:file_pk>/<str:field>', idea_img_page, name="userupload_idea_img_page"),
	path('file/<slug:redirect_name>/<int:obj_pk>/<slug:file_pk>/', delete_page, name="userupload_delete_page"),
] 