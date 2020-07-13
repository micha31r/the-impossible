from django.core.mail import send_mail
from django.conf import settings

def register_email(username,email):
    subject = 'Joined The Impossible'
    message = f"""
    	Hi {username}, thanks for joining The Impossible. \n
    	If you have any questions, please contact hello@theimpossible.world or write us a message from our website. \n
    	You will recieved a weekly update about the latest ideas by email. This can be changed in your newsletter settings. \n
    	\n
    	Regards 
    	The Impossible @ 2020
    """
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, email)
    return redirect('redirect to a new page')