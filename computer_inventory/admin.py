from django.contrib import admin
from .models import Computer
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Computer)

class ViewAdmin(ImportExportModelAdmin):
    pass
