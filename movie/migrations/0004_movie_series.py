# Generated by Django 3.1 on 2020-08-31 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200831_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='series_movie', to='movie.series'),
            preserve_default=False,
        ),
    ]
