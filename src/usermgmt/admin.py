from django.contrib import admin
from .models import (
	Notification,
	Profile,
)

class NotificationAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('__str__','message_status','dismissed','id','timestamp')
    readonly_fields = ["timestamp"]

class ProfileAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('user','timestamp','daily_limit','daily_limit_timestamp')
    readonly_fields = ["timestamp"]

admin.site.register(Notification,NotificationAdmin)
admin.site.register(Profile,ProfileAdmin)
