from import_export import resources
from .models import Student


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ['bits_id']
        import_id_fields = ['bits_id']
        exclude = ('id', )
        skip_unchanged = True
        report_skipped = True
