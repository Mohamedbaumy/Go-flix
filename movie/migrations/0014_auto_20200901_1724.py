# Generated by Django 3.1 on 2020-09-01 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_auto_20200901_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(default='fake', on_delete=django.db.models.deletion.CASCADE, to='movie.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='category',
            field=models.ForeignKey(default='jdkas', on_delete=django.db.models.deletion.CASCADE, to='movie.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
