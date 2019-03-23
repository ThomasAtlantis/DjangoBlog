from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Demo(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='./photos', default='./photos/none.jpg')
    href = models.CharField(max_length=100, default='#')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
