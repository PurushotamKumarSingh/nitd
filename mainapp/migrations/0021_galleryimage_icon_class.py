# Generated by Django 4.2.7 on 2024-01-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_remove_galleryimage_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='icon_class',
            field=models.CharField(default='fab fa-instagram', max_length=50),
        ),
    ]
