from django import forms

from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    model = ChatMessage
    fields = ['message']