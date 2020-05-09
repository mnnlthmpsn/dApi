from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('awaiting-confirmation/', views.registration, name='registration'),
    path('login/', views.authLogin, name='login'),
    path('category/', views.category, name='category'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/<uuid:category_id>/update/', views.update_category, name='update_category'),
    path('course/', views.course, name='course'),
    path('course/add/', views.add_course, name='add_course'),
    path('course/<uuid:course_id>/update/', views.update_course, name='update_course'),
    path('dashboard/', views.dashboard, name='dashboard'),
]