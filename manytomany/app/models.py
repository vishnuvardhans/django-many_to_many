# models.py
from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.student_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    def __str__(self):
        return self.course_name
