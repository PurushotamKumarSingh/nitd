# Generated by Django 4.2.7 on 2024-02-16 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_remove_blogpost_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Footer_Address',
        ),
        migrations.DeleteModel(
            name='Nav_Contact',
        ),
    ]
