from django.db import models
from student.models import Student
from .models import *
from .choices import subjects_CHOICES, etapa_CHOICES
import datetime
# Create your models here.


class Selenium(models.Model):
    subject = models.CharField(
        choices=subjects_CHOICES, max_length=20, default='Math')
    etapa = models.CharField(choices=etapa_CHOICES, max_length=1, default='1')
    marks = models.IntegerField(blank=True, null=True)

class Etapa(models.Model):
    etapa = models.CharField(choices=etapa_CHOICES,max_length=1,default='1')

    def __str__(self):
        return self.etapa + " Etapa"
class Exam(models.Model):
    description = models.CharField(max_length=30, null=True)
    total_value = models.IntegerField()
    subject = models.CharField(
        choices=subjects_CHOICES, max_length=20, default='Math')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,related_name='etapas')
    marks = models.IntegerField(blank=True, null=False,default=0)
    start = models.DateTimeField()
    end = models.DateTimeField()
    warning_date = models.DateField()
    all_day = models.BooleanField(default=False)
    owner = models.ForeignKey(Student, editable=False,
                              on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.description 


class Content(models.Model):
    learning_objects = models.CharField(max_length=190)
    skill = models.CharField(max_length=170)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,related_name='content_exam')

    def __str__(self):
        return str(str(self.learning_objects).split(' ')[0])
