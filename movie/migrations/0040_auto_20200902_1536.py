# Generated by Django 3.1 on 2020-09-02 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0039_episode_link_360'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='link_144',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='link_144',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='link_240',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='link_360',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='link_480',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='link_720',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='link_hd',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='link_240',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='link_480',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='link_720',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='link_hd',
        ),
    ]