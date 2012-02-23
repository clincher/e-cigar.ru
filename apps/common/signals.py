from django.conf import settings
from django.core.mail.message import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.feedback.models import Feedback


@receiver(post_save, sender=Feedback)
def feedback_notifying(sender, **kwargs):
    feedback = kwargs['instance']
    owners = getattr(settings, 'SN_OWNERS', settings.ADMINS)
    recipients = [owner[1] for owner in owners]
    subject = 'feedback: ' + feedback.subject
    body = feedback.text
    from_email = getattr(settings, 'SN_FROM_EMAIL',
                         settings.DEFAULT_FROM_EMAIL)
    headers = {'Reply-To': feedback.email}
    
    EmailMessage(subject, body, from_email, recipients, headers=headers).send()
