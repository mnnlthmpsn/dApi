from rest_framework import serializers
from .models import Category, Course, Topic, Content

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'code', 'description', 'date_published', 'is_popular')


class TopicSerializer(serializers.ModelSerializer):

    course = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'course', 'title', 'description')

class ContentSerializer(serializers.ModelSerializer):

    topic = serializers.CharField(source='topic.title', read_only=True)

    class Meta:
        model = Content
        fields = ('id', 'topic', 'content')