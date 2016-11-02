# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class News(models.Model):

    category = models.ForeignKey('Category',verbose_name=u'分类')
    tags = models.ManyToManyField('Tags', verbose_name=u'标签')

    title = models.CharField(max_length=123, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'内容')
    author = models.CharField(max_length=20, verbose_name=u'作者')

    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)




class Category(models.Model):

    name = models.CharField(max_length=20, verbose_name=u'分类名')

    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)


class Tags(models.Model):

    name = models.CharField(max_length=20, verbose_name=u'标签')

    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)






































































