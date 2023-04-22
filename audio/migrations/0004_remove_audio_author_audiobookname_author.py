# Generated by Django 4.2 on 2023-04-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_audio_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='author',
        ),
        migrations.AddField(
            model_name='audiobookname',
            name='author',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
