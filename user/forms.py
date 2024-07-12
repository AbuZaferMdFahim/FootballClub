# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(max_length=500, required=False, help_text='Optional. Tell us a little about yourself.')
    avatar = forms.ImageField(required=False, help_text='Optional. Upload a profile picture.')
    mobile = forms.CharField(max_length=15, required=False, help_text='Optional. Enter your mobile number.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'bio', 'avatar', 'mobile')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'mobile', 'avatar']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'mobile']
