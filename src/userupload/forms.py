from django import forms
from .models import (
    File,
    Link
)
 
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = [
            "description",
            "file",
        ]
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Description (Max 120)'})
        }
        labels={
            "description":"",
            "file":""
        }


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = [
            "description",
            "link",
        ]
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Description (Max 120)'})
        }
        labels={
            "description":"",
            "link":""
        }
