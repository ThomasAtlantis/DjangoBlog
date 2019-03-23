from django.contrib import admin
from .models import Demo
# Register your models here.

class DemoAdmin(admin.ModelAdmin):
	pass
admin.site.register(Demo, admin_class=DemoAdmin)
