import re
from django.conf import settings
from background_task import background
from templated_email import send_templated_mail

def at_filter(data):
	usernames = []
	for word in data.split(" "):
		if "@" in word:
			usernames.append(word.split("@")[-1])
	return usernames

# Escape HTML codes
# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def escape_html(raw_html):
	cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext


# Send email to users every week
def explore_email(email,username,question_id):
    send_templated_mail(
        template_name='question',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        context={
            'username':username,
            'question_id':question_id,
        },
	)

# explore_email(user.id, repeat=Task.WEEKLY, repeat_until=None)
