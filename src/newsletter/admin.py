from django.contrib import admin

from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('email',"last_sent","timestamp")

    readonly_fields = ["timestamp"]

admin.site.register(Subscriber,SubscriberAdmin)
