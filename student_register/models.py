from django.db import models

# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    student_number = models.CharField(max_length=3)
    student_class = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
