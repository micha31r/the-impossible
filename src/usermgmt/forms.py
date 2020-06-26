from django.forms import ModelForm, TextInput, PasswordInput
from django import forms

from .models import Profile

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

class ProfileForm(forms.Form):
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
    email = forms.EmailField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Email"
            }
        )
    )
    bio = forms.CharField(
        max_length=160,
        widget=forms.Textarea(
            attrs={
                "placeholder":"Bio (160)"
            }
        ),
        required=False
    )
    website = forms.URLField(
        max_length=160,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Website"
            }
        ),
        required=False
    )
    location = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Location (Planet Earth?)"
            }
        ),
        required=False
    )

class SettingForm(forms.ModelForm):
    tags_remain = forms.CharField(label="Exsisting Tags",required=False)
    blocked_user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"Type @username to block"
            }
        ),
        required=False
    )

    class Meta:
        model = Profile
        fields = [
            "tags",
            "like_setting",
            "comment_setting",
            "discover_setting",
        ]
        labels={
            "tags":"Tags",
            "like_setting":"Likes",
            "comment_setting":"Comments",
            "discover_setting":"Discover",
        }

class PasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Current Password"
            }
        ),
        required=False
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"New Password"
            }
        ),
        required=False
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Confirm Password"
            }
        ),
        required=False
    )