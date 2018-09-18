# -*- coding:utf-8 -
from django.db import models
from articles.models import Article

class Comments(models.Model):
	user_name = models.CharField('评论者名字', max_length=100)
	body = models.TextField('评论内容')
	created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
	article = models.ForeignKey(Article, verbose_name='评论所属文章', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.body[:20]
