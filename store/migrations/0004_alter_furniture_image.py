# Generated by Django 5.0.4 on 2024-05-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210403_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
