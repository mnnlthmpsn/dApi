from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('awaiting-confirmation/', views.registration, name='registration'),
    path('login/', views.authLogin, name='login'),
    path('category/', views.category, name='category'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/<uuid:category_id>/update/', views.update_category, name='update_category'),
    path('content/', views.content, name='content'),
    path('content/add/', views.add_content, name='add_content'),
    path('content/<uuid:content_id>/update/', views.update_content, name='update_content'),
    path('course/', views.course, name='course'),
    path('course/add/', views.add_course, name='add_course'),
    path('course/<uuid:course_id>/update/', views.update_course, name='update_course'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('topic/', views.topic, name='topic'),
    path('topic/add/', views.add_topic, name='add_topic'),
    path('topic/<uuid:topic_id>/update/', views.update_topic, name='update_topic'),
    path('settings/', views.settings, name='settings'),
    path('settings/update/', views.update_settings, name='update_settings'),
    path('settings/update/profile/', views.update_profile, name='update_profile'),
]