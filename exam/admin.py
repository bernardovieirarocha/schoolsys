from django.contrib import admin
from .models import Exam,Content,Etapa

#book = exam
#author = skill

class ContentInline(admin.TabularInline):
    model = Content


class ExamAdmin(admin.ModelAdmin):
    inlines = [ContentInline]

# Register your models here.
admin.site.register(Exam,ExamAdmin)
admin.site.register(Content)
admin.site.register(Etapa)