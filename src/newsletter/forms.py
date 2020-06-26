from django.forms import ModelForm, TextInput, PasswordInput
from django import forms

from .models import Subscriber

class SettingForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = [
            "frequency",
        ]
        labels={
            "frequency":"Email Frequency",
        }