from .models import SUPPORTED_FILE_TYPE, File

# get file extension
def file_extension(name):
	return (name.split(".")[-1]).lower()

def file_is_valid(name,expected_type):
	# Return file type
	extension = file_extension(name)

	# If given an expected file type
	if expected_type != "None":
		# Remove all symbols from text
		expected_type = ''.join(ch for ch in expected_type if ch.isalnum())
		if expected_type in SUPPORTED_FILE_TYPE.keys():
			for v in SUPPORTED_FILE_TYPE[expected_type]:
				if extension == v:
					return True

	# Else if file type is valid
	else:
		for k,v in SUPPORTED_FILE_TYPE.items():
			if extension in v:
				return True
	return False

# Remove foregin key or many to many reference and delete file
def file_validate_or_remove(obj,referred_obj_field,expected_file_type):
	globals()[referred_obj_field] = referred_obj_field
	try:
		if file_extension(getattr(obj,globals()[referred_obj_field]).file.name) not in SUPPORTED_FILE_TYPE[expected_file_type]:
			file_pk = getattr(obj,globals()[referred_obj_field]).id
			setattr(obj,globals()[referred_obj_field],None)
			file = File.objects.filter(pk=file_pk).first()
			file.file.delete(save=True)
			file.delete()
			return True
	except:
		try:
			for file in getattr(obj,globals()[referred_obj_field]).all():
				if file_extension(file.file.name) not in SUPPORTED_FILE_TYPE[expected_file_type]:
					getattr(obj,globals()[referred_obj_field]).remove(file)
					file.file.delete(save=True)
					file.delete()
					return True
		except: pass
	return False