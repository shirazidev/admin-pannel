from django.contrib import admin
from .models import iteams
from import_export.admin import ImportExportActionModelAdmin

@admin.register(iteams)
class iteamsAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'info')