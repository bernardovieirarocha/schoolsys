from django.shortcuts import render
from .models import Event
from .forms import  *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import  DetailView,View
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
import datetime
import json
from django.http import HttpResponse,JsonResponse



def calendar(request):
    all_events = Event.objects.all()
    print(all_events)

    events = [{
        "title": evento.title,
        "start": evento.start,
        "end": evento.end,
        "all_day":  evento.all_day,
        "evento_id": str(evento.id),
    } for evento in all_events]
    print(events)
    url_redirect = "{% url"
    return render(request,'calendar/fullcalendar.html',{"events":events,"url_redirect":url_redirect})


# class EventDetailView(LoginRequiredMixin,DetailView):
#   model = Event
#   context_object_name = 'student'


class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    template_name = "calendar/calendar_delete.html"
    success_url = reverse_lazy('calendar')

#TODO: Remove LoginRequired!
class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    form_class = EventForm
    template_name = 'calendar/calendar_create.html'
    success_url = '/calendar'

    def form_valid(self, form):
        context = self.get_context_data()
        with transaction.atomic():
            form.instance.owner = self.request.user
            self.object = form.save()
        return super(EventCreateView, self).form_valid(form)



class EventUpdate(LoginRequiredMixin,UpdateView):
    model = Event
    template_name = 'calendar/calendar_form.html'
    form_class = EventForm
    success_url = reverse_lazy('calendar')