from django.forms import ModelForm, TextInput, PasswordInput
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"Username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Password"
            }
        )
    )