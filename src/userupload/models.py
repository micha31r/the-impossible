from django.db import models
from usermgmt.models import Profile

from the_impossible.utils import *

SUPPORTED_FILE_TYPE = {
	"video":[
		"mp4",
		"mov",
		"webm"
	],
	"image":[
		"png",
		"jpg",
		"gif",
		"svg"
	],
	"other":[ 
		"zip"
	]
}

def user_directory_path(instance,filename):
	date = Date()
	extension = filename.split(".")[-1] 
	return f'uploaded/userid_{instance.user.id}/{extension}/{date.year()}/{date.month()}/{date.day()}/{filename}'

class File(models.Model):
	user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
	description = models.CharField(max_length=100)
	file = models.FileField(upload_to=user_directory_path)
	# Timestamp
	timestamp = models.DateTimeField(auto_now_add=True) 
	last_edit = models.DateTimeField(auto_now=True)

