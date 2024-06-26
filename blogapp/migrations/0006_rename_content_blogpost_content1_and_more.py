# Generated by Django 4.2.4 on 2024-02-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_blogpost_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='content',
            new_name='content1',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image2',
            field=models.ImageField(default='', upload_to='blog_images/'),
        ),
    ]
