"""schoolsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import*

urlpatterns = [
    path('', calendar, name='calendar'),
    path("create_event/",EventCreateView.as_view(),name='create_event'),
    path("deletar_event/<int:pk>/",EventDeleteView.as_view(),name='delete_event'),
    path('update_event/<int:pk>/',EventUpdate.as_view(),name='update_event')
] 
