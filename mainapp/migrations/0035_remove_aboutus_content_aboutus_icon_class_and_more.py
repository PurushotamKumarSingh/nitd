# Generated by Django 4.2.7 on 2024-01-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0034_aboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='content',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='icon_class',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
    ]