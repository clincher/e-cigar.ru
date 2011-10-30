from django import forms

from models import Callback


class CallbackForm(forms.ModelForm):
    """The form shown when giving callback"""
    class Meta:
        model = Callback
        exclude = ['site']