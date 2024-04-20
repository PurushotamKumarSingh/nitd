# Generated by Django 4.2.7 on 2024-01-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_timelineevent_content_timelineevent_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline_Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='timelineevent',
            name='content',
        ),
        migrations.RemoveField(
            model_name='timelineevent',
            name='subtitle',
        ),
    ]
