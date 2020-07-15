import datetime
from django.conf import settings
from background_task import background
from background_task.models import Task
from templated_email import send_templated_mail

from newsletter.models import Subscriber

from the_impossible.utils import *

# Send email to users every week
@background(schedule=0)
def explore_email():
	date = Date()
	today = date.now()
	timestamp = today - datetime.timedelta(days=7)

	# Free gmail account can only send 500 per day
	email_sum = 500

	"""
		Split weekly_subs evenly with monthly_subs, 
		pick 250 weekly and monthly subscribers per day.
		If there are less than 250 weekly subscribers, then 
		increase the number of monthly subscribers.
	"""
	weekly_subs = Subscriber.objects.filter(
		last_sent__lt = timestamp,
		frequency = 2
	).exclude(frequency=1).distinct()[:250] 
	email_sum -= weekly_subs.count()
	
	monthly_subs = Subscriber.objects.filter(
		last_sent__lt = timestamp,
		frequency = 3
	).exclude(frequency=1).distinct()[:email_sum] 

	subscribers = weekly_subs | monthly_subs

	# Must send email one by one to keep users' email address hidden
	for sub in subscribers:
		send_templated_mail(
			template_name='question',
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[sub.email],
			context={
			    'username':"micha31r",
			    'question_id':12383,
			},
		)
		sub.last_sent = today
		sub.save()

explore_email(repeat=Task.DAILY, repeat_until=None)