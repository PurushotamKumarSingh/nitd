# Generated by Django 4.2.7 on 2024-01-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration_icon_class',
            field=models.CharField(default='fas fa-calendar-alt', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor_icon_class',
            field=models.CharField(default='fas fa-user', max_length=50),
        ),
    ]
