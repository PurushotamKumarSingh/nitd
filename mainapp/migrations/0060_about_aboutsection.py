# Generated by Django 4.2.4 on 2024-02-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0059_home_aboutsection_course_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='about_section/')),
                ('about_image', models.ImageField(upload_to='about_section/')),
                ('video_url', models.URLField(default=' ')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('trainer_count', models.IntegerField(default=1, help_text='Enter the number of Trainers')),
                ('students_count', models.IntegerField(default=1, help_text='Enter the number of Students')),
                ('course_count', models.IntegerField(default=1, help_text='Enter the number of Courses offered')),
                ('seminar_count', models.IntegerField(default=1, help_text='Enter the number of Seminar Conduct')),
            ],
        ),
    ]
