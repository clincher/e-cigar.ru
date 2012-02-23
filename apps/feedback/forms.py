#!/usr/bin/env python
from django import forms
from captcha.fields import CaptchaField

from models import Feedback


class FeedbackForm(forms.ModelForm):
    '''The form shown when giving feedback'''
    captcha = CaptchaField()
    
    class Meta:
        model = Feedback
