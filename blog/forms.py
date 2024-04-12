from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
    Allows a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


