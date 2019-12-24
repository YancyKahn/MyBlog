# Generated by Django 2.1.1 on 2019-06-12 16:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='collected',
            field=models.ManyToManyField(blank=True, related_name='collected_videos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked_videos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='view_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterModelTable(
            name='video',
            table='v_video',
        ),
    ]