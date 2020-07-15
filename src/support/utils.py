from django.core.mail import send_mail
from django.conf import settings
from background_task import background
from django.contrib.auth.models import User

from templated_email import send_templated_mail

from .models import CoreFeed

# This creates private system feed
def create_corefeed(option,**kwargs):
	# A list of all system core feed messages:
	CORE_FEED = {
		# Auth
		"WELCOME":{
			"name":"Welcome to The Impossible",
			"description":f"""
				<a href="{kwargs["absolute_url"]}">@{kwargs["username"]}</a> 
				Thanks for joining us. Create, share and explore fresh ideas. 
				As a social media platform, we want our service to be as transparent 
				as possible, therefore, here is the information we store about you:
				<ul>
					<li>Full Name</li>
					<li>Email Address</li>
					<li>Website</li>
					<li>Profile Image</li>
					<li>Location</li>
					<li>Followers and Following</li>
				</ul>
				Lastly, if you wish to terminate your account, 
				please email <a href="mailto: hello@theimpossible.world">\"hello@theimpossible.world\"</a>. 
				(All data will be deleted)

			"""
		}
	}
	obj = CoreFeed.objects.create(
		name = CORE_FEED[option]["name"],
		description = CORE_FEED[option]["description"]
	)
	obj.save()
	return obj

@background(schedule=20)
def support_email(email,username,question_id):
    send_templated_mail(
        template_name='question',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        context={
            'username':username,
            'question_id':question_id,
        },
	)
