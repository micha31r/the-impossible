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

class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder":"First Name"
            }
        )
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Last Name"
            }
        )
    )
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Username"
            }
        )
    )
    email = forms.EmailField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Email"
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
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Confirm Password"
            }
        )
    )