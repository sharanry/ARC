from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.

from main.models import Student, CDC, CourseSlot, Output

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from main.actions import single_option_CDC


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    search_fields = ['CAMPUS_ID', "NAME", "YEAR", "DISC"]
    actions = [single_option_CDC,]

@admin.register(CDC)
class CDCAdmin(ImportExportModelAdmin):
    resource_class = CDCResource
    search_fields = ['comp_codes', 'course_code']


@admin.register(CourseSlot)
class CourseSlotAdmin(ImportExportModelAdmin):
    resource_class = CourseSlotResource
    search_fields = ['class_nbr', 'course_id']

@admin.register(Output)
class OutputAdmin(ImportExportModelAdmin):
    resource_class = OutputResource
    search_fields = ['CAMPUS_ID', 'CATALOG_NBR', 'CLASS_NBR', 'CLASS_SECTION', 'CRSE_ID', 'DESCR', 'EMPLID', 'SUBJECT']


admin.site.site_header = "Academic Registration & Counselling Division"

admin.site.site_title = "Academic Registration & Counselling Division"




# Filter

class EntityAdmin(ImportExportModelAdmin):
    ...
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
    )