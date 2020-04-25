from django.forms import ModelForm, TextInput, Textarea
from django import forms

from .models import *

class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = [
            "name",
            "short_description",
            "full_description",
            "tags",
            "publish_stats"
        ]
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Title (Max 80)'}),
            'short_description': Textarea(attrs={'placeholder': 'Description (Max 150)'}),
            'full_description': Textarea(attrs={'placeholder': 'Content (Max 2000)'}),
        }
        labels={
            "name":"",
            "short_description":"",
            "full_description":"",
            "tags":"Tags",
            "publish_stats":"Publish Status",
        }