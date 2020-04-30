from django.contrib import admin
from .models import Category, Course, Topic, Content

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Content)