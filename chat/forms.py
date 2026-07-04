from django import forms
from .models import Message
from django.contrib.auth.forms import AuthenticationForm

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            "usermessage",
            "textmessage",
        )

