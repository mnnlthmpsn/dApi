from uuid import uuid4
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, default='Please enter title of course category... eg. Business')
    description = models.CharField(max_length=200, null=False, default='Please enter description for category')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, default='Computer Science')
    code = models.CharField(max_length=10, null=False, default='DZCS101')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=False, default='This is is DZCS101')
    date_published = models.DateTimeField(auto_now_add=True)
    is_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return ('{0} : {1}'.format(self.title, self.code))


class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, default='Computer Science')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=False, default='This is is DZCS101')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE)
    content = RichTextField()

    def __str__(self):
        return str(self.id)