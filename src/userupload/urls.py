from django.urls import path

from .views import (
	file_page
)

urlpatterns = [
	path(
		'file/<slug:pk>/<str:referred_obj_name>/<int:referred_obj_pk>/<str:referred_obj_field>/<slug:expected_file_type>', 
		file_page, 
		name="userupload_file_page"
	),
] 