# Generated by Django 4.2.7 on 2024-02-10 15:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_contact', message='Contact must be a 10-digit number.', regex='^\\d{10}$')])),
                ('image_url', models.ImageField(default=' ', upload_to='logo_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png'])])),
            ],
        ),
    ]
