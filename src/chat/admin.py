from django.contrib import admin
from .models import ChatGroup, ChatMessage

class ChatGroupAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('name','owner','member_count','id','timestamp')
        
    search_fields = ('name',)

    def member_count(self,obj):
        return obj.member.all().count()

    readonly_fields = ["timestamp"]

class ChatMessageAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('user','to_user','to_group','id','timestamp')
        
    search_fields = ('name',)

    readonly_fields = ["timestamp"]

admin.site.register(ChatGroup,ChatGroupAdmin)
admin.site.register(ChatMessage,ChatMessageAdmin)
