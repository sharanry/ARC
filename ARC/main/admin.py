from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from main.models import Student, Course, CourseSlot

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    search_fields = ['bitsId']


# admin.site.register(Student, StudentAdmin)
