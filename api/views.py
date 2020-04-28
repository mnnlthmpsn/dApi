from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CategorySerializer, CourseSerializer, TopicSerializer
from .models import Category, Course, Topic


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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

    @action(detail=True, methods=['get'])
    def topics(self, request, pk=None):
        # .../id/topics/ gets all topics related to a particular course
        course = get_object_or_404(Course, pk=pk)
        topics = course.topic_set.all()
        serializer = self.get_serializer(topics, many=True)
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
    permission_classes = [permissions.IsAdminUser]