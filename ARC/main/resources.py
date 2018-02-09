from import_export import resources
from .models import Student, CDC, CourseSlot


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        import_id_fields = ['id']
        fields = ['id', 'CAMPUS_ID', 'NAME', 'YEAR', 'DISC']
        # exclude = ('id', )
        # skip_unchanged = True
        # report_skipped = True


class CDCResource(resources.ModelResource):
    class Meta:
        model = CDC
        import_id_fields = ['comp_codes']
        fields = ['comp_codes', 'course_code', 'tag',
                  'course_name', 'units', 'year', 'sem']


class CourseSlotResource(resources.ModelResource):
    class Meta:
        model = CourseSlot
        import_id_fields = ['class_nbr']
        fields = [	'subject',
                   'class_nbr',
                   'section',
                   'room',
                   'class_pattern',
                   'mtg_start',
                   'end_time',
                   'instructor_ID',
                   'instructor_name',
                   'instructor_role',
                   'exam_tm_cd',
                   'exam_date',
                   'course_admin',
                   ]
