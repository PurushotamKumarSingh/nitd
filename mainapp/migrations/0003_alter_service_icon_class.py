# Generated by Django 4.2.7 on 2024-01-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_homeslider_image_keypoint_keyservice_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon_class',
            field=models.CharField(max_length=50),
        ),
    ]
