from django import forms
from .models import *

class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']