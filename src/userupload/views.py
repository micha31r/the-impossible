from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *

from idea.models import Idea

from the_impossible.utils import *

from the_impossible.ERROR import *

from .utils import *

from .forms import (
	FileForm
)

@login_required
def file_page(request, pk, referred_obj_name, referred_obj_pk, referred_obj_field, expected_file_type):
	ctx = {} # Context variables
	ctx["date"] = Date()
	ctx["obj"] = obj = get_object_or_404(globals()[referred_obj_name], pk=referred_obj_pk)
	ctx["file"] = file = File.objects.filter(pk=pk.isdigit() and pk or -1).first()
	ctx["form"] = form = FileForm(request.POST or None, request.FILES or None)
	if obj.author.user == request.user:
		# Set default values
		if file:
			form.fields["description"].initial = file.description
			form.fields["file"].initial = file.file

			# Return file type
			for k,v in SUPPORTED_FILE_TYPE.items():
				if file_extension(file.file.name) in v:
					ctx['file_type'] = k
					break

		if form.is_valid():
			uploaded_file = request.FILES.get("file")
			if uploaded_file:
				if file_is_valid(uploaded_file.name,expected_file_type):	
					data = form.cleaned_data

					# Create file
					if not file:
						file = File.objects.create(
							user=request.user,
							description = data.get("description"),
							file = uploaded_file
						)
					else: # replace file
						file.description = form.cleaned_data.get("description")
						file.file = uploaded_file
						file.save()
					file.save()

					# Link file to parent object
					globals()[referred_obj_field] = referred_obj_field
					try: setattr(obj,globals()[referred_obj_field],file) # Set Foregin key field
					except: 
						try: getattr(obj,globals()[referred_obj_field]).add(file) # Add to many to many field 
						except: pass
					obj.save()
					return redirect(f"{referred_obj_name.lower()}_edit_page",pk=referred_obj_pk)
				
				# Invalid file type
				else:
					ctx["error"] = SERVER_ERROR["FILE"]

			# If user didn't replace the old file
			elif file.file:
				return redirect(f"{referred_obj_name.lower()}_edit_page",pk=referred_obj_pk)
	else:
		return redirect("access_error_page")
	template_file = "userupload/file_page.html"
	return render(request,template_file,ctx)

