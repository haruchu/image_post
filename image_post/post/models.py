from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.

class Image(models.Model):
    image = models.ImageField(
        validators=[FileExtensionValidator(['png', 'jpg'])], upload_to="images")
    title = models.CharField(max_length=30)
    file_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
