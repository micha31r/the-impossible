from django.urls import path

from .views import (
	join_view,
)

urlpatterns = [
	path('join/', join_view, name="newsletter_join_view"),
] 