# Generated by Django 4.2.4 on 2024-02-11 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0048_contact_contactform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='About_Testimonials',
        ),
        migrations.RenameModel(
            old_name='TestimonialsSection',
            new_name='About_TestimonialsSection',
        ),
    ]