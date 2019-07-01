from django import forms
from .models import Post, Comment, Star


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['content', 'image']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = ['rate']