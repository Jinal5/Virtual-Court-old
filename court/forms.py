from django.contrib.auth.models import User
from django import forms
from .models import *

CHOICES = [
    ("Judge", "Judge"),
    ("Lawyer", "Lawyer"),
]
Court_Type=[
    ("SUP","Supreme Court"),
    ("HIG","High Court"),
    ("DST","District Court"),
    ("SES","Session Court"),
]

class UserForm(forms.ModelForm):
<<<<<<< HEAD
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    user_type = forms.ChoiceField(choices=CHOICES)
    court = forms.MultipleChoiceField(choices = Court_Type,required=True,widget=forms.CheckboxSelectMultiple)
    address = forms.CharField(max_length=500, required=True)
    license_no = forms.CharField(min_length=15, max_length=17, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Bar ID'}))
=======
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=CHOICES)
    court = forms.MultipleChoiceField(choices = Court_Type,required=True,widget=forms.CheckboxSelectMultiple)
    address = forms.CharField(max_length=500, required=True)
    license_no = forms.CharField(min_length=15, max_length=17, required=True)
>>>>>>> 80025140d39514c1cc78f16240f96bad1ab73e05

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
            "address",
            "license_no",
        ]


class LoginForm(forms.ModelForm):
<<<<<<< HEAD
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
=======
    password = forms.CharField(widget=forms.PasswordInput)
>>>>>>> 80025140d39514c1cc78f16240f96bad1ab73e05

    class Meta:
        model = User
        fields = ["username", "password"]

class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = [
            "advocate",
            "name_of_applicant",
            "phone_number",
            "address",
            "case_type",
            "court_type",
            "subject",
            "file",
            "district",
            "state",
            "name_of_respondent",
            "lawyer_of_respondent",
            "address_of_respondent",
        ]
<<<<<<< HEAD
        exclude = ('advocate',)


class MultipleForm(forms.ModelForm):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class UsernForm(MultipleForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    user_type = forms.ChoiceField(choices=CHOICES)
    court = forms.MultipleChoiceField(choices = Court_Type,required=True,widget=forms.CheckboxSelectMultiple)
    address = forms.CharField(max_length=500, required=True)
    license_no = forms.CharField(min_length=15, max_length=17, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Bar ID'}))

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
            "address",
            "license_no",
        ]

class LoginnForm(MultipleForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = ["username", "password"]

    
        exclude = ('advocate','status','cnr','fileNo')
=======
        exclude = ('advocate','status','cnr','fileNo','judge')
>>>>>>> 80025140d39514c1cc78f16240f96bad1ab73e05


class SearchForm(forms.ModelForm):
    cnr=forms.CharField(max_length=16, required=True)
    class Meta:
        model = Case
        fields=[
            "cnr",
<<<<<<< HEAD
        ]

class FeesForm(forms.Form):
    court = forms.CharField(max_length=50)
    case = forms.CharField(max_length=50)
    subtype = forms.CharField(max_length=50)

=======
        ]
>>>>>>> 80025140d39514c1cc78f16240f96bad1ab73e05
