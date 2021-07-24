from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']