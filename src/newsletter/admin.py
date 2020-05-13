from django.contrib import admin

from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('email',"last_sent","timestamp")

    readonly_fields = ["timestamp"]

admin.site.register(Newsletter,NewsletterAdmin)
