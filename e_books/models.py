# -*- coding: UTF-8 -*-
from django.db import models
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
# Create your models here.
class E_Book(models.Model):
	KIND_CHOICES = (
		('科幻作品', '科幻作品'),
		('科普书籍', '科普书籍'),
		('文化艺术', '文化艺术'),
		('技术文章', '技术文章'),
		('参考资料', '参考资料'),
		('其他书籍', '其他书籍'),
	)
	title = models.CharField(max_length=100)
	kind = models.CharField(max_length=20, choices=KIND_CHOICES, default='其他书籍')
	fileName = models.FileField(upload_to = './e_books/', default="")
	description = models.TextField(default="", blank=True)
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
