from django.contrib import admin
from projects.models import project,users,s_project
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(project)
class projectAdmin(ImportExportModelAdmin):
	
	pass

@admin.register(users)
class usersAdmin(ImportExportModelAdmin):
	filter_horizontal = ('p_submitted',)
	pass

@admin.register(s_project)
class s_projectAdmin(admin.ModelAdmin):
	pass