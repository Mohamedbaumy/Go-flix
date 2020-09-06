# Generated by Django 3.1 on 2020-09-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0022_auto_20200901_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slug_movie',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_series',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
