from django.contrib import admin
from home.models import Wiki
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Wiki)
class wiki(ImportExportModelAdmin):
    pass
