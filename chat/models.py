from django.db import models
from django.dispatch import receiver 
from django.conf import settings
from datetime import date


class Chat(models.Model):
    created_at = models.DateField(default=date.today)
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recevier_message_set')

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)

