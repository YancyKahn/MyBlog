# Generated by Django 2.1.1 on 2019-06-13 09:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('0', '发布中'), ('1', '未发布')], max_length=1, null=True)),
                ('title', models.CharField(default='', max_length=50, verbose_name='article')),
                ('content', models.TextField(verbose_name='context')),
                ('digest', models.TextField(default='', verbose_name='descript')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='create_time')),
                ('edit_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='update_time')),
                ('read_nums', models.IntegerField(default=0, verbose_name='read_nums')),
                ('image', models.ImageField(upload_to='blog/%Y/%m', verbose_name='cover')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'db_table': 'a_blog',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'a_classification',
            },
        ),
        migrations.CreateModel(
            name='Tagprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'a_tag',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Classification', verbose_name='classification'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.Tagprofile'),
        ),
    ]
