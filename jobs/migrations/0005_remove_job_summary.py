# Generated by Django 2.0.2 on 2020-05-21 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_merge_20200521_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='summary',
        ),
    ]
