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

"""
Although the universal view function is more DRY oriented, 
I am using seperate view functions as they are more easiers to maintain
and easier to add features.
"""

# A universal view function for file upload
"""
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
				# This only work if the url name starts with the model's name. E.G: idea_edit_page
				return redirect(f"{referred_obj_name.lower()}_edit_page",pk=referred_obj_pk)
	else:
		return redirect("access_error_page")
	template_file = "userupload/file_page.html"
	return render(request,template_file,ctx)
"""

@login_required
def idea_img_page(request,idea_pk,file_pk,field):
	ctx = {} # Context variables
	ctx["date"] = Date()
	ctx["file"] = file = File.objects.filter(pk=file_pk.isdigit() and file_pk or -1).first()
	ctx["form"] = form = FileForm(request.POST or None, request.FILES or None)
	ctx["redirect_name"] = redirect_name = "idea_edit_page"

	ctx["obj"] = idea = get_object_or_404(Idea, pk=idea_pk)

	if idea.author.user == request.user:
		# Set default values
		if file:
			form.fields["description"].initial = file.description
			form.fields["file"].initial = file.file

		if form.is_valid():
			uploaded_file = request.FILES.get("file")
			if uploaded_file:
				if file_is_valid(uploaded_file.name,"image"):	
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
					if field == "header":
						idea.header_img = file
					elif field == "body":
						idea.body_img.add(file)
					idea.save()
					return redirect(redirect_name,pk=idea_pk)

				# Invalid file type
				else:
					ctx["error"] = SERVER_ERROR["FILE"]
			# If user didn't replace the old file
			elif file.file:
				# This only work if the url name starts with the model's name. E.G: idea_edit_page
				return redirect(redirect_name,pk=idea_pk)
	else:
		return redirect("access_error_page")
	template_file = "userupload/img_page.html"
	return render(request,template_file,ctx)

@login_required
def delete_page(request,redirect_name,obj_pk,file_pk):
	file = get_object_or_404(File, pk=file_pk)
	file.delete()
	return redirect(redirect_name,pk=obj_pk)
	
