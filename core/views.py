from __future__ import unicode_literals
from django.shortcuts import render
from exam.models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser # <-- Here
from rest_framework import serializers
from rest_framework import status
# Create your views here.


class CategoryListView(APIView):
    # Only Admin token works if IsAdminUser is on the permission_classes
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)


class ExamListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_queryset(self):
        return super(ExamListView, self).get_queryset().filter(owner=self.request.user)

class EventListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return super(EventListView, self).get_queryset().filter(owner=self.request.user)

# class MusicianView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MusicianSerializer
#     queryset = Musician.objects.all()


class ContentListView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


# class AlbumView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AlbumSerializer
#     queryset = Album.objects.all()

