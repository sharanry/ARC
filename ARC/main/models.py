from django.db import models

# Create your models here.


class Student(models.Model):
    bits_id = models.CharField(max_length=13, primary_key=True)


class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    # course_slot =


class CourseSlot(models.Model):
    DAYS = {
        ('M', 'Monday'),
        ('Tu', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday')
    }
    days = models.CharField(max_length=2, choices=DAYS)
    # time_slot = models.CahrField()
