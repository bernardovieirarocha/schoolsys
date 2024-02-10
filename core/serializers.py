from rest_framework import serializers, fields
from exam.models import Exam, Content
from calendar_app.models import Event,Category
from rest_framework.fields import CurrentUserDefault
from django.shortcuts import get_object_or_404
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Event
        fields = ['title','start','end','category','all_day']

    def create(self, validated_data):
        user = self.context['request'].user
        category_data = validated_data.pop('category')
        category = get_object_or_404(Category,name=category_data['name'])
        evento = Event.objects.create(owner=user,category=category,**validated_data)
        return evento


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id','learning_objects', 'skill']

class ExamSerializer(serializers.ModelSerializer):
    content_exam = ContentSerializer(many=True)
    class Meta:

        model = Exam
        fields = ('id','description', 'total_value', 'subject', 'etapa',
                  'marks', 'start', 'end', 'warning_date', 'all_day', 'content_exam')
        # exclude = ['owner']

    def create(self, validated_data):
        user = self.context['request'].user
        contents_data = validated_data.pop('content_exam')
        exam = Exam.objects.create(owner=user,**validated_data)
        for content_data in contents_data:
            Content.objects.create(exam=exam, **content_data)
        return exam

    # def update(self, instance, validated_data):
    #     contents_data = validated_data.pop('contents')
    #     contents = (instance.contents).all()
    #     contents = list(contents)
    #     instance.learning_objects = validated_data.get('learning_objects', instance.learning_objects)
    #     instance.skill = validated_data.get('skill', instance.skill)
    #     instance.exam = validated_data.get('exam', instance.exam)
    #     instance.save()

    #     for content_data in contents_data:
    #         content = albums.pop(0)
    #         content.name = album_data.get('name', album.name)
    #         album.release_date = album_data.get('release_date', album.release_date)
    #         album.num_stars = album_data.get('num_stars', album.num_stars)
    #         album.save()
    #     return instance

