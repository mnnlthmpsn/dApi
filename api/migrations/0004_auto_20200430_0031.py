# Generated by Django 3.0.5 on 2020-04-30 07:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200430_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]