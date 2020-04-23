from django.forms import ModelForm, TextInput, Textarea
from django import forms

class IdeaForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"Title"
            }
        ),
        required=False,
        label=""
    )
    short_description = forms.CharField(
       	widget=forms.Textarea(
            attrs={
                "placeholder":"Short description"
            }
        ),
        required=False,
        label=""
    )
    full_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder":"Content"
            }
        ),
        required=False,
        label=""
    )