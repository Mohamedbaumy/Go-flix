# Generated by Django 3.1 on 2020-09-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20200831_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='age',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='description',
        ),
        migrations.AddField(
            model_name='series',
            name='age',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(default='about'),
            preserve_default=False,
        ),
    ]