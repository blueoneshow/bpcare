# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models

#留言板的格式
class Message(models.Model):
        user = models.CharField(max_length=50)
        subject = models.CharField(max_length=200)
        publication_date = models.DateTimeField()
        
        def __unicode__(self):
                return self.subject
          
# 日誌
class Diary(models.Model):
        memo = models.TextField()
        time = models.DateTimeField(auto_now_add=True)
      
        def __unicode__(self):
                return self.memo

# 月份
class Month(models.Model):
        date = models.IntegerField(default=0)
    
        def __unicode__(self):
                return str(self.date)
        
# 帳目
class Money(models.Model):
        kind = models.IntegerField(default=0)
        item = models.IntegerField(default=0)       
        price = models.IntegerField(default=0)
        time = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
                return self.item
          
#測試
class Test(models.Model):
  user = models.CharField(max_length=50)
  subject = models.CharField(max_length=200)
  memo = models.TextField()
  
  def __unicode__(self):
    return self.subject
  