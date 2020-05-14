from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse

from .models import Subscriber

def email_is_valid(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def join_view(request):
	data = {}
	email = request.GET.get('email', None)
	if email_is_valid(email) and request.is_ajax():
		exsisting_emails = Subscriber.objects.filter(email=email)
		# Check if email is already used
		for obj in exsisting_emails:
			print(obj)
			if obj.email == email:
				data['exsist'] = True
		if 'exsist' not in data:
			obj = Subscriber.objects.create(email=email,frequency=2)
			obj.save()
	else:
		data['failed'] = True
	return JsonResponse(data)

