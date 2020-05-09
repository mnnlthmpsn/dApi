from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .serializers import CategorySerializer, CourseSerializer, TopicSerializer, ContentSerializer
from .models import Category, Course, Topic, Content

from django.core.exceptions import ObjectDoesNotExist


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        # .../id/courses/ gets all courses related to a particular category
        category = get_object_or_404(Category, pk=pk)
        courses = category.course_set.all().order_by('title')
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def topics(self, request, pk=None):
        # .../id/topics/ gets all topics related to a particular course
        course = get_object_or_404(Course, pk=pk)
        topics = course.topic_set.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    # course/popular/
    def popular(self, request):
        courses = Course.objects.filter(is_popular=True)
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # topic/id/content
    @action(detail=True, methods=['get'])
    def contents(self, request, pk=None):
        topic = get_object_or_404(Topic, pk=pk)
        contents = topic.content
        serializer = ContentSerializer(contents)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_next(self, request, pk=None):
        topic = get_object_or_404(Topic, pk=pk)
        try:
            next_topic = topic.get_next_by_pub_date()
            serializer = TopicSerializer(next_topic)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(None)

    @action(detail=True, methods=['get'])
    def get_previous(self, request, pk=None):
        topic = get_object_or_404(Topic, pk=pk)
        try:
            previous_topic = topic.get_previous_by_pub_date()
            serializer = TopicSerializer(previous_topic)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(None)

        

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]