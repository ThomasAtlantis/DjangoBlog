# -*- coding: UTF-8 -*-
from django.db import models
import sys;
import Tag
reload(sys);
sys.setdefaultencoding("utf8")

# Create your models here.
class Films(models.Model):
    KIND_CHOICES = (
        ('科幻电影', '科幻电影'),
        ('魔幻电影', '魔幻电影'),
        ('美剧英剧', '美剧英剧'),
		('其他类型', '其他类型')
    )
    title = models.CharField(max_length=100)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default="其他类型")
    video_url = models.CharField(max_length=100)
    introduction_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

