from django.urls import path
from django.conf import settings

from .views import (
	join_view,
	email_page,
)

urlpatterns = [
	path('join/', join_view, name="newsletter_join_view"),
] 

if settings.DEBUG:
	# THIS IS FOR TESTING ONLY !!
	urlpatterns.append(path('email/', email_page, name="newsletter_email_page"))