from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django_thumbs.db.models import ImageWithThumbsField

@python_2_unicode_compatible
class Gallery(models.Model):
    title = models.CharField(max_length=250, blank=True)
    original = ImageWithThumbsField(upload_to='./photos', default='./photos/none.jpg', sizes=((240, 180),))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

