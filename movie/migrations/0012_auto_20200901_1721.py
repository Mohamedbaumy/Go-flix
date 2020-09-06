# Generated by Django 3.1 on 2020-09-01 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20200901_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.category'),
        ),
        migrations.AlterField(
            model_name='series',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.category'),
        ),
    ]
