# Generated by Django 3.0.5 on 2020-05-01 05:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Please enter title of course category... eg. Business', max_length=100)),
                ('description', models.CharField(default='Please enter description for category', max_length=200)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Computer Science', max_length=100)),
                ('code', models.CharField(default='DZCS101', max_length=10)),
                ('description', models.CharField(default='This is is DZCS101', max_length=200)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('is_popular', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Computer Science', max_length=100)),
                ('description', models.CharField(default='This is is DZCS101', max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', ckeditor.fields.RichTextField()),
                ('topic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Topic')),
            ],
        ),
    ]
