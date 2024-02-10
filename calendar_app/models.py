from django.db import models
from exam.models import *



class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=30, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    category = models.ForeignKey(Category,related_name='categorias',
                                on_delete=models.PROTECT)
    owner = models.ForeignKey(Student, editable=False,
                              on_delete=models.SET_NULL, blank=True, null=True)
    all_day = models.BooleanField(default=False)

    def __str__(self):
        return self.title
