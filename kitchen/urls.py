from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('awaiting-confirmation/', views.registration, name='registration'),
    path('login/', views.authLogin, name='login'),

    # categories/departments
    path('category/', views.category, name='category'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/<uuid:category_id>/details/', views.category_details, name='category_details'),
    path('category/<uuid:category_id>/update/', views.update_category, name='update_category'),

    # contents
    path('content/<uuid:course_id>/add/', views.add_content, name='add_content'),
    path('content/<uuid:course_id>/<uuid:topic_id>/update', views.update_content, name='update_content'),

    # courses
    path('course/<uuid:category_id>/add/', views.add_course, name='add_course'),
    path('course/<uuid:course_id>/update/', views.update_course, name='update_course'),
    path('course/<uuid:course_id>/details/', views.course_details, name='course_details'),

    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # settings
    path('settings/', views.settings, name='settings'),
    path('settings/update/', views.update_settings, name='update_settings'),
    path('settings/update/profile/', views.update_profile, name='update_profile'),
]