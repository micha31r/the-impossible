from django.contrib import admin
from .models import (
    ChatGroup,
    ChatPermission,
    ChatMessage,
)

class ChatGroupAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('name','owner','member_count','id','timestamp')
        
    search_fields = ('name',)

    def member_count(self,obj):
        return obj.member.all().count()

    readonly_fields = ["timestamp"]

class ChatPermissionAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('user','group','permitted','id','timestamp')
        
    search_fields = ('user',)

    readonly_fields = ["timestamp"]

class ChatMessageAdmin(admin.ModelAdmin):
    # Display custom fields in Django admin
    list_display = ('user','message','id','timestamp')
        
    search_fields = ('user',)

    readonly_fields = ["timestamp"]

admin.site.register(ChatGroup,ChatGroupAdmin)
admin.site.register(ChatPermission,ChatPermissionAdmin)
admin.site.register(ChatMessage,ChatMessageAdmin)
