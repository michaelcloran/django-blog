from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Allows a form to be displayed for collaboration
    with name email and message fields
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')