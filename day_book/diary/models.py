
from django.db import models
import os
# Create your models here.
from rest_framework.exceptions import ValidationError

class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    age = models.IntegerField(blank=True, null=False)
    grade = models.IntegerField(blank=True, null=False)
    attendance = models.BooleanField(blank=True, null=False, default=True)
    homework = models.BooleanField(blank=True, null=False, default=True)


class Group(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)


class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    age = models.IntegerField(blank=True, null=False)
    subject = models.CharField(max_length=50, blank=True, null=False)
    group_id = models.OneToOneField(Group, on_delete=models.CASCADE, null=True, blank=True)





class Message(models.Model):
    body = models.TextField(blank=True, null=False)
    phone = models.IntegerField(blank=True, null=False)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True)
