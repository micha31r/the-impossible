from django.urls import path

from .views import (
	signup_page,
	login_page,
	logout_view,
	account_dashboard_page,
	account_notification_page,
	account_follow_view,
	account_profile_page,
	account_setting_page,
)

urlpatterns = [
	path('signup/', signup_page, name="signup_page"),
	path('login/', login_page, name="login_page"),
	path('logout/', logout_view, name="logout_view"),
	path('account/dashboard/<slug:username>/<str:content_filter>/<int:page_num>/', account_dashboard_page, name="account_dashboard_page"),
	path('account/notification/<int:page_num>/', account_notification_page, name="account_notification_page"),
	path('account/follow/<slug:username>/', account_follow_view, name="account_follow_view"),
	path('account/settings/profile', account_profile_page, name="account_profile_page"),
	path('account/settings/', account_setting_page, name="account_setting_page"),
]
