from django.contrib import admin
from .models import (
	Idea,
)

class IdeaAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('name','id','timestamp')
    readonly_fields = ["timestamp"]

admin.site.register(Idea,IdeaAdmin)