# Generated by Django 3.1 on 2020-09-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0020_auto_20200901_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.RemoveField(
            model_name='series',
            name='category',
        ),
    ]
