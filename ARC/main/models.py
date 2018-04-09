from django.db import models


class Student(models.Model):
    """
    from GTA
    """
    id = models.CharField(max_length=11, primary_key=True, blank=True)
    CAMPUS_ID = models.CharField(max_length=13, null=True)
    NAME = models.CharField(max_length=100, null=True)
    YEAR = models.CharField(max_length=4, null=True)
    DISC = models.CharField(max_length=4, null=True)

    def __str__(self):
        return "%s %s" % (self.CAMPUS_ID, self.NAME)



class CDC(models.Model):
    """ from "CDC File" """
    # Course ID in CourseTT
    comp_codes = models.CharField(max_length=5, primary_key=True, blank=True)
    course_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=5, )
    course_name = models.CharField(max_length=30)
    units = models.CharField(max_length=2, null=True)
    year = models.CharField(max_length=4, null=True)
    sem = models.CharField(max_length=1, null=True)

    def __str__(self):
        return "%s %s %s" % (self.comp_codes, self.course_code, self.course_name)


class CourseSlot(models.Model):

    # CDC = models.ForeignKey(CDC, on_delete=models.PROTECT, null=True)
    course_id = models.CharField(max_length=6, blank=True)
    # subject = models.CharField(max_length=5, null=True)
    # catalog = models.CharField(max_length=4, )
    class_nbr = models.CharField(max_length=4, primary_key=True, blank=True)
    section = models.CharField(max_length=2, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.course_id, self.section, self.class_nbr, get_cdc(self.course_id[1:]))

     # room = models.CharField(max_length=10, null=True)

    # Class Pattern
    # class_pattern = models.CharField(max_length=4, null=True)
    # TODO: Make more robust

    # mtg_start = models.TimeField(null=True)
    # end_time = models.TimeField(null=True)

    # instructor_ID = models.CharField(max_length=20, null=True)
    # instructor_name = models.CharField(max_length=30, null=True)
    # instructor_role = models.CharField(max_length=2, null=True)

    # exam_tm_cd = models.CharField(max_length=5, null=True)
    # exam_date = models.DateField(null=True)

    # course_admin = models.CharField(max_length=5, null=True)

    # days = models.CharField(max_length=10, choices=DAYS)
    # time_slot = models.CahrField()


class Output(models.Model):
    EMPLID = models.CharField(max_length=11, blank=True)
    CAMPUS_ID = models.CharField(max_length=13, null=True)
    CRSE_ID = models.IntegerField(null=True)
    SUBJECT = models.CharField(max_length=6, null=True)
    CATALOG_NBR = models.CharField(max_length=4, null=True)
    DESCR = models.CharField(max_length=20, null=True)
    CLASS_NBR = models.IntegerField(null=True)
    CLASS_SECTION = models.CharField(max_length=5, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.EMPLID, self.CAMPUS_ID, self.DESCR, self.CLASS_SECTION)


class Map(models.Model):
    name = models.CharField(max_length=20)
    courseSlots = models.ManyToManyField(CourseSlot)

    def __str__(self):
        return "%s" % (self.name)

# class Students(models.Model):
#     # name = models.CharField(max_length=20)
#     students = models.ManyToManyField(Student)

#     def __str__(self):
#         return "%s" % (self.name)

# helper functions
def get_cdc(comp_code):
    try:
        return CDC.objects.get(comp_codes__contains=comp_code).course_name
    except CDC.DoesNotExist:
        return None
