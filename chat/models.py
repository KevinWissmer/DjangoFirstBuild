from django.db import models
from django.dispatch import receiver
from django.db.models.fields import DateField
from django.conf import settings
from datetime import date

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = DateField(default=date.today)
    #chat = chatklasse link
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recevier_message_set')