from django.contrib import admin
from .models import Thread, ChatMessage, ThreadMembership

# Register your models here.
admin.site.register(Thread)
admin.site.register(ChatMessage)
admin.site.register(ThreadMembership)