from django.contrib import admin
from .models import (
	Feedback,
	Question,
	CoreFeed
)

class FeedbackAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('author','__str__','viewed','id','timestamp')
    readonly_fields = ["timestamp"]

class QuestionAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('author','short_description','solved','id','timestamp')
    readonly_fields = ["timestamp"]

class CoreFeedAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('name','publish_status','id','timestamp')
    readonly_fields = ["timestamp"]

admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(CoreFeed,CoreFeedAdmin)