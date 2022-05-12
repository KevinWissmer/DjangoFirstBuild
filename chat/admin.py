from django.contrib import admin
from chat.models import Message, Chat



class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'author', 'chat', )
    list_display = ('author', 'text', 'receiver', 'chat',)
    list_filter = ('created_at',)
    search_fields = ('text','author',)

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Message, MessageAdmin)


class ChatAdmin(admin.ModelAdmin):
    fields = ('created_at', )
    list_display = ('created_at', )
    list_filter = ('created_at',)
    #search_fields = ('created_at', )

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Chat, ChatAdmin)
