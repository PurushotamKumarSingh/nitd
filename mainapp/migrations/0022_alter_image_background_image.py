# Generated by Django 4.2.7 on 2024-01-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_galleryimage_icon_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='background_image',
            field=models.ImageField(upload_to='background_images/'),
        ),
    ]
