from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.

from main.models import Student, CDC, CourseSlot

# From GTA


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    search_fields = ['bitsId']


@admin.register(CDC)
class CDCAdmin(ImportExportModelAdmin):
    resource_class = CDCResource
    search_fields = ['comp_codes', 'course_code']


@admin.register(CourseSlot)
class CourseSlotAdmin(ImportExportModelAdmin):
    resource_class = CourseSlotResource
    search_fields = ['subject']

# admin.site.register(Student, StudentAdmin)


admin.site.site_header = "Academic Registration & Counselling Division"

admin.site.site_title = "Academic Registration & Counselling Division"
