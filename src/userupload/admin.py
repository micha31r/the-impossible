from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
	# Display custom fields in Django admin
	list_display = ("file_name","file_extension","user","timestamp","last_edit")

	def file_name(self,obj):
		name = obj.file.name.split("/")[-1].split(".")[0]
		if len(name) > 20:
			name = name[:20] + "..."
		return name

	def file_extension(self,obj):
		extension = obj.file.name.split("/")[-1].split(".")[-1]
		return extension

	readonly_fields = ["timestamp"]


admin.site.register(File,FileAdmin)