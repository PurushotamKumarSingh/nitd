# Generated by Django 4.2.4 on 2024-02-12 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0053_coursedetail_course_coursedetail_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail_course',
            name='image',
            field=models.ImageField(default='', upload_to='course_detail_images/'),
        ),
    ]