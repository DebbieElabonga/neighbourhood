from django import forms
from django.contrib.auth.models import User
from .models import Profile,Post


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')