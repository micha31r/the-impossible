from django.core.mail import send_mail
from django.conf import settings

def email_welcome(username,email):
    subject = 'Joined The Impossible'
    message = f"""
    	Hi @{username}, thanks for joining The Impossible.
    	If you have any questions, please contact hello@theimpossible.world or write us a message from our website.
    	You will recieved a weekly update about the latest ideas by email. This can be changed in your newsletter settings.

    	Regards
    	The Impossible @ 2020
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    try:
    	send_mail(subject, message, email_from, recipient_list)
    except: pass

def all_private_notification(qs):
    all_private = True
    for notification in qs:
        if notification.message_status != 1:
            all_private = False
            break
    return all_private