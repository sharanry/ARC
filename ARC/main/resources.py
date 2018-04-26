from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Student, CDC, CourseSlot, Output


# from .utils import TimeWidget, DateWidget, CompCodesWidget


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        import_id_fields = ['id']
        fields = ['id', 'CAMPUS_ID', 'NAME', 'YEAR', 'DISC']


class CDCResource(resources.ModelResource):
    class Meta:
        model = CDC
        import_id_fields = ['comp_codes']
        fields = [
            'comp_codes',
            'course_code',
            'tag',
            'course_name',
            'units',
            'year',
            'sem'
        ]
        exclude = ('id', )


class OutputResource(resources.ModelResource):
    class Meta:
        model = Output

        exclude = ('id', )


class CourseSlotResource(resources.ModelResource):

    class Meta:
        model = CourseSlot

        import_id_fields = ['class_nbr']
        fields = [
            'course_id',
            'class_nbr', #CRSE_ID
            'section', #CLASS_SECTION
            'subject', #SUBJECT
            'catalog', #CATALOG_NBR
            'course_title', #DESCR
            ]
        