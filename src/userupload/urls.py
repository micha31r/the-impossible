from django.urls import path

from .views import (
	idea_header_img_page,
	idea_body_img_page,
	delete_page
)

urlpatterns = [
	path('file/idea/header/<int:idea_pk>/<slug:file_pk>/', idea_header_img_page, name="userupload_idea_header_img_page"),
	path('file/idea/body/<int:idea_pk>/<slug:file_pk>/', idea_body_img_page, name="userupload_idea_body_img_page"),
	path('file/<slug:redirect_name>/<int:obj_pk>/<slug:file_pk>/', delete_page, name="userupload_delete_page"),
] 