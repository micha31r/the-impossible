from .models import SUPPORTED_FILE_TYPE, File

# get file extension
def file_extension(name):
	return name.split(".")[-1] 

def file_is_valid(name):
	# Return file type
	for k,v in SUPPORTED_FILE_TYPE.items():
		if file_extension(name) not in v:
			return False
	return True

# Remove foregin key or many to many reference and delete file
def file_validate_or_remove(obj,referred_obj_field,expected_file_type):
	globals()[referred_obj_field] = referred_obj_field
	try:
		if file_extension(getattr(obj,globals()[referred_obj_field]).file.name) not in SUPPORTED_FILE_TYPE[expected_file_type]:
			file_pk = getattr(obj,globals()[referred_obj_field]).id
			setattr(obj,globals()[referred_obj_field],None)
			file = File.objects.filter(pk=file_pk).first()
			file.delete()
	except:
		try:
			for file in getattr(obj,globals()[referred_obj_field]).all():
				if file_extension(file.file.name) not in SUPPORTED_FILE_TYPE[expected_file_type]:
					getattr(obj,globals()[referred_obj_field]).remove(file)
					file.delete()
		except: pass