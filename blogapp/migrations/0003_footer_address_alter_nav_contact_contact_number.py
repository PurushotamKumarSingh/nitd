# Generated by Django 4.2.7 on 2024-02-10 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_nav_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='nav_contact',
            name='contact_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='invalid_contact', message='Contact must be a 10-digit number.', regex='^\\d{10}$')]),
        ),
    ]