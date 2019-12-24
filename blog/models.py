import os
from datetime import datetime
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from user.models import User

class BlogQuerySet(models.query.QuerySet):

    def get_count(self):
        return self.count()

    def get_published_count(self):
        return self.filter(status=0).count()

    def get_not_published_count(self):
        return self.filter(status=1).count()

    def get_published_list(self):
        return self.filter(status=0).order_by('-create_time')

    def get_search_list(self, q):
        if q:
            return self.filter(title__contains=q).order_by('-create_time')
        else:
            return self.order_by('-create_time')

    def get_recommend_list(self):
        return self.filter(status=0).order_by('-view_count')[:4]


class Classification(models.Model):
    list_display = ("title",)
    title = models.CharField(max_length=100,blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "a_classification"



class Tagprofile(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = "a_tag"


class Blog(models.Model):
    #博客文章
    STATUS_CHOICES = (
        ('0', '发布中'),
        ('1', '未发布'),
    )

    status = models.CharField(max_length=1 ,choices=STATUS_CHOICES, blank=True, null=True)
    title = models.CharField(verbose_name='title', max_length=50,default='')
    category = models.ForeignKey(Classification,on_delete=models.CASCADE,null=True,verbose_name='category')
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='author')
    content = models.TextField(verbose_name='content')
    digest = models.TextField(verbose_name='digest',default='')
    create_time = models.DateTimeField(verbose_name='create_time',default=datetime.now)
    edit_time = models.DateTimeField(verbose_name='edit_time',default=datetime.now)
    view_count = models.IntegerField(verbose_name='view_count', default=0)
    #comment_nums = models.IntegerField(verbose_name='评论数', default=0)
    cover = models.ImageField(verbose_name='cover', upload_to='blog/%Y/%m',blank=True, null=True)
    tag = models.ManyToManyField(Tagprofile)

    objects = BlogQuerySet.as_manager()
    class Meta:
        db_table = "a_blog"

    def __str__(self):
        return self.title

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

@receiver(models.signals.post_delete, sender=Blog)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    删除FileField文件
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
