# Generated by Django 3.1 on 2020-09-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0041_auto_20200902_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug_movie',
            field=models.SlugField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug_series',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
