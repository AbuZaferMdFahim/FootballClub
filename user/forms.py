# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(max_length=500, required=False, help_text='Optional. Tell us a little about yourself.')
    avatar = forms.ImageField(required=False, help_text='Optional. Upload a profile picture.')
    mobile = forms.CharField(max_length=15, required=False, help_text='Optional. Enter your mobile number.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'bio', 'avatar', 'mobile')
