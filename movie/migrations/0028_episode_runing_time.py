# Generated by Django 3.1 on 2020-09-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0027_auto_20200901_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='runing_time',
            field=models.PositiveIntegerField(default=120),
        ),
    ]
