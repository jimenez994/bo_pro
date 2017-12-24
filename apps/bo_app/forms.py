from django import forms 
from .models import *

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','image']