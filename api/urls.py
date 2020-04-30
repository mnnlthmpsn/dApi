from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'course', views.CourseViewSet, basename='course')
router.register(r'topic', views.TopicViewSet, basename='topic')
router.register(r'content', views.ContentViewSet, basename='content')

urlpatterns = [
    path('', include(router.urls)),
]