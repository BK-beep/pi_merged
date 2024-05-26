from django.db import models
from django.conf import settings

class Conversation(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(
            Conversation,
            on_delete=models.CASCADE
        )

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ('created_at',)