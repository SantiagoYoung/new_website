# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class About_us(models.Model):
    title = models.CharField(max_length=12,verbose_name=u'标题')
    description  = models.TextField(verbose_name=u'描述')
    picture = models.ImageField(upload_to='about/', null=True, blank=True)
    display = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'关于我们'
        verbose_name_plural =u'关于我们'

    def __unicode__(self):
        return self.title

class History(models.Model):
    about = models.ForeignKey(About_us)

    year = models.CharField(max_length=12, verbose_name=u'年限')
    description = models.TextField(verbose_name=u'公司经历')

    class Meta:
        verbose_name_plural = u'历史'
        verbose_name = u'历史'


    def __unicode__(self):
        return self.year


class Facts(models.Model):
    about = models.ForeignKey(About_us)

    picture = models.ImageField(upload_to='facts/',verbose_name=u'成就')
    title = models.CharField(max_length=20, verbose_name=u'事迹名称')
    description = models.TextField(verbose_name=u'事迹描述')
    create_time = models.DateTimeField(default=datetime.now())
    edit_time = models.DateTimeField(auto_now=True)
    display = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = u'事迹'
        verbose_name = u'事迹'

    def __unicode__(self):
        return self.title


class QnA(models.Model):
    about = models.ForeignKey(About_us)

    question = models.CharField(max_length=100, verbose_name=u'问题名称')
    answer = models.TextField(verbose_name=u'回答')
    display = models.BooleanField(default=False)
    create_time = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'问题&答复'
        verbose_name_plural = u'问题&答复'

    def __unicode__(self):
        return self.question