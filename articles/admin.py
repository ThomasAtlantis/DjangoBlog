from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	# class Media:
	# 	css = {'all':(
	# 		'css/simditor.css',
	# 	)}
	# 	js = (
	# 		'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
 #            'js/simditor/module.js',
 #            'js/simditor/uploader.js',
 #            'js/simditor/hotkeys.js',
 #            'js/simditor/simditor.js',
 #            'js/rich_text.js',
	# 	)
	class Media:
	    js = (
	        '/static/js/kindeditor/kindeditor-all-min.js',
	        '/static/js/kindeditor/lang/zh-CN.js',
	        '/static/js/kindeditor/config.js',
	    )

admin.site.register(Article, admin_class=ArticleAdmin)
