from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from main.models import Student, Course, CourseSlot

from django.utils.translation import ugettext_lazy

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    search_fields = ['bitsId']


# admin.site.register(Student, StudentAdmin)

admin.site.site_header = "Academic Research Division"