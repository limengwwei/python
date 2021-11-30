from django.db import models
from django.utils.timezone import now
# Create your models here.
class Photo(models.Model):
    image   = models.ImageField(upload_to='photo/%Y%m%d/')
    created = models.DateTimeField(default=now)

    def __str__(self):
        return self.image.name
    class Meta:
        ordering = ('-created',)