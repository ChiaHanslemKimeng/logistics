from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Shipment

@receiver(post_save, sender=Shipment)
def send_shipment_notification(sender, instance, created, **kwargs):
    if created:
        try:
            subject = f'Shipment Alert: {instance.tracking_number} is on the way!'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = instance.receiver_email
            
            # Context for the email
            tracking_url = f"http://127.0.0.1:8000/track/?number={instance.tracking_number}"
            context = {
                'shipment': instance,
                'tracking_url': tracking_url,
            }
            
            # Render HTML and plain text versions
            html_content = render_to_string('emails/shipment_notification.html', context)
            text_content = strip_tags(html_content)
            
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            
            print(f"Notification email sent to {to_email} for shipment {instance.tracking_number}")
        except Exception as e:
            print(f"Failed to send email: {e}")
