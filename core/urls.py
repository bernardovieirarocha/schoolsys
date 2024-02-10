"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core.views import *
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import url
urlpatterns = [
    # URL to get the token auth, work for every user but only admin tokens get or post data
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # URL to POST or GET musics 
    url(r'^exams/$', ExamListView.as_view(), name='exams-list'),
    url(r'^events/$', EventListView.as_view(), name='events-list'),
    url(r'^categorys/$', CategoryListView.as_view(), name='categories-list')
]

