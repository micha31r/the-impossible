from django import forms
from .models import (
    Tag,
    Idea
)

class IdeaForm(forms.ModelForm):
    tags_remain = forms.CharField(label="",required=False)

    class Meta:
        model = Idea
        fields = [
            "name",
            "short_description",
            "full_description",
            "tags",
            "publish_stats",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Title (Max 80)'}),
            'short_description': forms.Textarea(attrs={'placeholder': 'Description (Max 150)'}),
            'full_description': forms.Textarea(attrs={'placeholder': 'Content (Max 2000)'}),
        }
        labels={
            "name":"",
            "short_description":"",
            "full_description":"",
            "tags":"Tags",
            "publish_stats":"Publish Status",
        }
