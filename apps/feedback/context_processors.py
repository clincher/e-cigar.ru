__author__ = 'goodfellow'

from forms import FeedbackForm

def feedback_form(request):
    return {'feedback_form': FeedbackForm()}