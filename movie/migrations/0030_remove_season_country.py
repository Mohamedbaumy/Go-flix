# Generated by Django 3.1 on 2020-09-01 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0029_season_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='country',
        ),
    ]