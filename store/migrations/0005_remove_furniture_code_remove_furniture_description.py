# Generated by Django 5.0.6 on 2024-05-12 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_furniture_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='code',
        ),
        migrations.RemoveField(
            model_name='furniture',
            name='description',
        ),
    ]
