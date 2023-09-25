import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(User, related_name='threads', through= 'ThreadMembership')

    def __str__(self):
        return f'Thread {self.id}'

class ThreadMembership(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['thread', 'user']

class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    sent_by =models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message in Thread {self.thread.id}'
    


































# class Thread(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     sent_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_sent_by')
#     received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_received_by')

#     class Meta:
#         unique_together = ['sent_by', 'received_by']

#     def __str__(self):
#         return f'Thread {self.id}'

# class ChatMessage(models.Model):
#     room = models.ForeignKey(Thread, on_delete=models.CASCADE)
#     message = models.TextField()
#     sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     sent_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'messages of room {self.room.id}'