# Generated by Django 4.2.4 on 2024-02-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0049_rename_testimonials_about_testimonials_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_CertifiedTrainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='certified_trainers/')),
                ('description', models.TextField()),
            ],
        ),
    ]
