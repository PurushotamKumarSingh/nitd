# Generated by Django 4.2.7 on 2024-01-07 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_rename_image_galleryimage_imagenext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryimage',
            old_name='imagenext',
            new_name='imagesnext',
        ),
    ]