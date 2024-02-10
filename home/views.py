from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request,'home.html')