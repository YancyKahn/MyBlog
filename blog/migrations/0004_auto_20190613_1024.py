# Generated by Django 2.1.1 on 2019-06-13 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190613_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='add_time',
        ),
        migrations.AddField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='create_time'),
        ),
    ]
