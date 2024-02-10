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
from django.urls import path
from .views import*

urlpatterns = [
    path('exam_create', ExamCreate.as_view(), name="exam_create"),
    path('exam_detail/<int:pk>/',ExamDetail.as_view(),name='exam_detail'),
    path("exam_update/<int:pk>/",ExamUpdate.as_view(),name='exam_update'),
    path('exam_list',ExamListView.as_view(),name='exam_list'),
    path("exam_delete/<int:pk>/",ExamDeleteView.as_view(template_name='exam/exam_delete_confirm.html'),name='exam_delete'),
    path('calendar/', calendar, name='calendar_exam'),

]
