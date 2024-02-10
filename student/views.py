from django.shortcuts import render,redirect
from  django.views.generic.list import ListView
from  django.views.generic.edit import DeleteView,UpdateView,CreateView
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse

class StudentListView(LoginRequiredMixin,ListView):
    model = Student

    def get_queryset(self):
      return self.model.objects.filter(password=self.request.user.password)

class StudentDetailView(LoginRequiredMixin,DetailView):
  model = Student
  context_object_name = 'student'



class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    template_name = "student/delete.html"
    success_url = reverse_lazy('student_list')

#TODO: Remove LoginRequired!
class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    form_class = RegisterForm
    success_url = '/students/list_student/'

