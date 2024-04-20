# Generated by Django 4.2.7 on 2024-01-11 06:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_missionvision_quote_alter_aboutsection_video_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_contact', message='Contact must be a 10-digit number.', regex='^\\d{10}$')]),
        ),
    ]