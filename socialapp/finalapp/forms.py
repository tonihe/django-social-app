from django import forms
from .models import *


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label = '',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'What\'s on your mind?'
        })
    )

    image = forms.ImageField(
        label= '', required=False)

    class Meta:
        model = Post
        fields = ['body', 'image']

    
    

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label = '',
        widget=forms.Textarea(attrs={
            'row': '3',
            'placeholder': 'Say something...'
        })
    )

    class Meta:
        model = Comment
        fields = ['comment']

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


class MessageForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000)

    image = forms.ImageField(required=False)

    class Meta:
        model = MessageModel
        fields = ['body', 'image']