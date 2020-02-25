from django import forms
from django.forms import ModelForm, Textarea
from .models import Blog, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BLogForm(forms.ModelForm):
    class Meta:
        exclude=("approved_blog","author","rank","countview")
        model = Blog


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )
        widgets = {
            'text':
            Textarea(attrs={
                'class': 'form-control z-depth-1',
                'rows': 7,
                'style': 'width:50%'
            }),
        }


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",'email')