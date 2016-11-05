# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime



class ArchiveManager(models.Manager):

    def archive(self):

        result = []
        all_date = self.values('create_time')
        for date in all_date:
            date = date['create_time'].strftime('%Y-%m')
            if date not in result:
                result.append(date)
        return result


class News(models.Model):

    category = models.ForeignKey('Category',verbose_name=u'分类')
    tags = models.ManyToManyField('Tags', verbose_name=u'标签')

    title = models.CharField(max_length=256, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'内容')
    author = models.CharField(max_length=256, verbose_name=u'作者')
    is_display = models.BooleanField(default=False, verbose_name=u'是否展示')
    click_num = models.IntegerField(default=0, verbose_name=u'点击量')


    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)


    objects = ArchiveManager()

    def clean_create_time(self):
        create_time = self.create_time.strftime('%Y-%m')
        return create_time



class Category(models.Model):

    name = models.CharField(max_length=256, verbose_name=u'分类名')

    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)


class Tags(models.Model):

    name = models.CharField(max_length=256, verbose_name=u'标签')

    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)






































































