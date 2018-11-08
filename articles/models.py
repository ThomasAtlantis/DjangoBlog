# -*- coding: UTF-8 -*-
from django.db import models
from Category.models import Category
from Tag.models import Tag
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag, related_name="tag_articles", 	blank=True)
	editor_type = models.BooleanField(default=True)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
