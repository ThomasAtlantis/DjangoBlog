from django.contrib import admin
from .models import Comments
# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
#    list_display = ('subject','mail','topic','message')
	pass
admin.site.register(Comments, CommentsAdmin)
