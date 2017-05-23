# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'姓名')
    sex = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')))

    class Meta:
        verbose_name = u'个人信息'
        verbose_name_plural = verbose_name
