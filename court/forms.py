from django.contrib.auth.models import User
from django import forms
from .models import *

CHOICES = [
    ("Judge", "Judge"),
    ("Lawyer", "Lawyer"),
]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.CharField(max_length=30, choices=CHOICES)
    court = forms.CharField(max_length=100, blank=False)
    district = forms.CharField(max_length=100, blank=False)
    license_no = forms.CharField(max_length=17, null=False)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password1",
            "email",
            "first_name",
            "last_name",
            "user_type",
            "court",
            "district",
            "license_no",
        ]


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]
