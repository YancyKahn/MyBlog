# Generated by Django 2.1.1 on 2019-06-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190613_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]
