# Generated by Django 3.0.5 on 2020-04-30 07:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', ckeditor.fields.RichTextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Topic')),
            ],
        ),
    ]