# Generated by Django 2.0.2 on 2020-05-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_remove_class_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_description',
            field=models.TextField(default='no description'),
            preserve_default=False,
        ),
    ]
