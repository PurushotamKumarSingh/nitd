# Generated by Django 4.2.7 on 2024-01-06 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_aboutsection_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutsection',
            name='video_url',
        ),
    ]
