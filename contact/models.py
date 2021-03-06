# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.





class Contact(models.Model):
    location  = models.CharField(max_length=30, verbose_name=u'地址')
    location_picture = models.ImageField(upload_to='contact/')
    email = models.EmailField(max_length=30, verbose_name=u'邮件')
    email_picture = models.ImageField(upload_to='contact/')
    phone = models.CharField(max_length=20, verbose_name=u'电话')
    phone_picture = models.ImageField(upload_to='contact/')
    # description = models.CharField(max_length=150, verbose_name=u'描述')

    class Meta:
        verbose_name_plural = u'联系'
        verbose_name =  u'联系'

    def __unicode__(self):
        return self.phone


class Message(models.Model):
    sender_name = models.CharField(max_length=30, verbose_name=u'发信人')
    sender_email = models.EmailField(max_length=30, verbose_name=u'发信人邮箱')
    phone = models.CharField(max_length=30, verbose_name=u'发送人电话')
    message = models.TextField(verbose_name=u'消息')
    title = models.CharField(max_length=20, verbose_name=u'标题')
    description = models.CharField(max_length=150, verbose_name=u'描述')

    class Meta:
        verbose_name_plural = u'信息'
        verbose_name = u'信息'

    def __unicode__(self):
        return self.sender_name





