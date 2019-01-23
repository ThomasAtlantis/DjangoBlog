# -*- coding: UTF-8 -*-
from django.db import models
from Category.models import Category
from Tag.models import Tag
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100, verbose_name="标题")
	category = models.ForeignKey(Category, verbose_name="分类")
	tag = models.ManyToManyField(Tag, related_name="tag_articles", 	blank=True, verbose_name="标签")
	editor_type = models.BooleanField(default=True, verbose_name="不使用MarkDown")
	body = models.TextField(verbose_name="内容")
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
