# Generated by Django 3.1 on 2020-09-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0025_auto_20200901_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='slug',
            field=models.SlugField(default='slug', max_length=250),
            preserve_default=False,
        ),
    ]