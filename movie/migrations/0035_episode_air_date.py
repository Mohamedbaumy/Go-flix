# Generated by Django 3.1 on 2020-09-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0034_remove_episode_air_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='air_date',
            field=models.DateField(default='2020-08-07'),
        ),
    ]
