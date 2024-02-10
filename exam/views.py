from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import  DetailView,View
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render,redirect
from django.views.generic.list import ListView

def calendar(request):
    all_events = Exam.objects.all()
    print(all_events)
    events = [{
        "title": evento.description,
        "start": evento.start,
        "end": evento.end,
        "all_day":  evento.all_day,
        "evento_id": str(evento.id),
    } for evento in all_events]
    print(events)
    url_redirect = "{% url"
    return render(request,'exam/exam_calendar.html',{"events":events,"url_redirect":url_redirect})



class ExamListView(LoginRequiredMixin,ListView):
    model = Exam
    template_name = "exam/exam_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Exam.objects.filter(owner=self.request.user).order_by('id')


class ExamCreate(LoginRequiredMixin,CreateView):
    model = Exam
    template_name = 'exam/exam_create.html'
    form_class = ExamForm
    success_url = 'exam_list'

    def get_context_data(self, **kwargs):
        data = super(ExamCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['skills'] = SkillFormSet(self.request.POST)
        else:
            data['skills'] = SkillFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        skills = context['skills']
        with transaction.atomic():
            form.instance.owner = self.request.user
            if form.instance.marks is None:
                form.instance.marks = 0
            self.object = form.save()
            if skills.is_valid():
                skills.instance = self.object
                skills.save()
        return super(ExamCreate, self).form_valid(form)


class ExamDetail(LoginRequiredMixin,DetailView):
    model = Exam
    template_name = 'exam/exam_detail.html'
    success_url = 'exam_list'


class ExamUpdate(LoginRequiredMixin,UpdateView):
    model = Exam
    template_name = 'exam/exam_create.html'
    form_class = ExamForm
    success_url = reverse_lazy('exam_list')

    def get_context_data(self, **kwargs):
        data = super(ExamUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['skills'] = SkillFormSet(self.request.POST,instance=self.object)
        else:
            data['skills'] = SkillFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        skills = context['skills']
        with transaction.atomic():
            form.instance.owner = self.request.user
            if form.instance.marks is None:
                form.instance.marks = 0
            self.object = form.save()
            if skills.is_valid():
                skills.instance = self.object
                skills.save()
        return super(ExamUpdate, self).form_valid(form)


class ExamDeleteView(LoginRequiredMixin,DeleteView):
    model = Exam
    template_name = "exam/exam_delete_confirm.html"
    success_url = reverse_lazy('exam_list')

