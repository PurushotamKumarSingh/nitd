# Generated by Django 4.2.7 on 2024-01-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_quoterequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslider',
            name='button_text',
            field=models.CharField(max_length=50),
        ),
    ]
