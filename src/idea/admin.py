from django.contrib import admin
from .models import (
	Idea,
)

class IdeaAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('name','id','timestamp',"view_count","like_count")
    
    def view_count(self,obj):
        return obj.viewed_user.all().count()

    def like_count(self,obj):
        return obj.liked_user.all().count()

    readonly_fields = ["timestamp"]

admin.site.register(Idea,IdeaAdmin)