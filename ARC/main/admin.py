from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from main.models import Student, CDC, CourseSlot

from django.utils.translation import ugettext_lazy

# From GTA
@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    search_fields = ['bitsId']



@admin.register(CDC)
class StudentAdmin(ImportExportModelAdmin):
    search_fields = ['course_code']


@admin.register(CourseSlot)
class StudentAdmin(ImportExportModelAdmin):
    search_fields = ['subject']

# admin.site.register(Student, StudentAdmin)


admin.site.site_header = "Academic Research Division"

admin.site.site_title = "Academic Research Division"
