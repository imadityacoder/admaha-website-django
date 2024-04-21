from django.core.mail import send_mail
from django.conf import settings

def send_admin_notification(post_sub:str,post_message:str):
    subject = post_sub
    message = post_message
    sender_email = settings.EMAIL_HOST_USER
    recipient_list = [admin_email for name, admin_email in settings.ADMINS]
    send_mail(subject, message, sender_email, recipient_list)

def send_user_notification(post_sub:str,post_message:str, user_email):
    subject = post_sub
    message = post_message
    sender_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, sender_email, recipient_list)