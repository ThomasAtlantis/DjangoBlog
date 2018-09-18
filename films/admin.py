from django.contrib import admin
from .models import Films

# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
        )

admin.site.register(Films, admin_class=FilmAdmin)

