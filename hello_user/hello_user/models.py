#-*-coding:utf-8-*-

from __future__ import unicode_literals
from django.db import models

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'

    def __unicode__(self):
        return self.name

class Tb2(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    groupname = models.CharField(max_length=20)

    class Meta:
        db_table = 'friendsList'
        verbose_name = '测试表'
        verbose_name_plural = '测试表'

    def __unicode__(self):
        return self.name
