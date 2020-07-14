from django.core.mail import send_mail
from django.conf import settings

def email_welcome(username,email):
    subject = 'Joined The Impossible'
    message = f"""
    	Hi @{username}, thanks for joining The Impossible. \n
    	If you have any questions, please contact hello@theimpossible.world or write us a message from our website. \n
    	You will recieved a weekly update about the latest ideas by email. This can be changed in your newsletter settings. \n
    	\n
    	Regards \n
    	The Impossible @ 2020
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    try:
    	send_mail(subject, message, email_from, recipient_list)
    except: pass