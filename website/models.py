# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime








class Service(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'服务', )
    description = models.TextField(verbose_name=u'服务描述')
    thumbnail = models.ImageField(upload_to='service/',verbose_name=u'头像')
    is_featured = models.BooleanField(default=False, verbose_name=u'优秀')
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name = u'服务'
        verbose_name_plural = u'服务'

    def __unicode__(self):
        return self.name



class Portfolio(models.Model):

    service = models.ForeignKey(Service)
    name = models.CharField(max_length=256, verbose_name=u'项目名称')
    description = models.TextField(verbose_name=u'项目描述')
    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='porfolio/')
    display = models.BooleanField(default=False, verbose_name=u'展示')

    class Meta:
        verbose_name = u'项目'
        verbose_name_plural = u'项目'

    def __unicode__(self):
        return self.name


class Carousel_figure(models.Model):

    title = models.CharField(max_length=256, verbose_name=u'标题')
    piture = models.ImageField(upload_to='carousel/')
    description = models.TextField(verbose_name=u'简介')
    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = u'轮播图'
        verbose_name =  u'轮播图'

    def __unicode__(self):
        return self.title

class Client_words(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'标题')
    client_name = models.CharField(max_length=256, verbose_name=u'客户名字')
    client_title = models.CharField(max_length=256, verbose_name=u'客户职位')
    client_company = models.CharField(max_length=256, verbose_name=u'客户公司')
    client_words = models.TextField(verbose_name=u'客户寄语')
    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='client/')
    display = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'客户寄语'
        verbose_name_plural = u'客户寄语'

    def __unicode__(self):
        return self.client_name



class Structure(models.Model):

    section = models.CharField(max_length=256, verbose_name=u'主题')
    description = models.TextField(verbose_name=u'主题描述')

    create_time = models.DateTimeField(default=datetime.now())


    class Meta:
        verbose_name_plural = u'分区'
        verbose_name = u'分区'

    def __unicode__(self):
        return self.section












































