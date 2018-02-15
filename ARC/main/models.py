from django.db import models

# Create your models here.


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
# from "CDC File"


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

        if self.CDC != None:
            return "%s %s %s " % (self.class_nbr, self.CDC.course_code, self.course.course_name)
        else:
            return "%s %s" % (self.course_id, self.class_nbr)

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