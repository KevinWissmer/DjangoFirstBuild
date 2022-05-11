from django.contrib import admin
from chat.models import Message



class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'author', 'receiver')
    list_display = ('author', 'text', 'receiver')
    list_filter = ('created_at',)
    search_fields = ('text','author',)

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Message, MessageAdmin)



