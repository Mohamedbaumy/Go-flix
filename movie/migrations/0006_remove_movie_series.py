# Generated by Django 3.1 on 2020-08-31 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200831_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='series',
        ),
    ]
