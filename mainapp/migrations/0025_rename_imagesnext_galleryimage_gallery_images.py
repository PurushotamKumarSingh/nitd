# Generated by Django 4.2.7 on 2024-01-07 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_rename_imagenext_galleryimage_imagesnext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryimage',
            old_name='imagesnext',
            new_name='gallery_images',
        ),
    ]