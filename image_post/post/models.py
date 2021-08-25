from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
import uuid

# Create your models here.
def image_path(instance, filename):
    return 'images/{}.{}'.format(str(instance.created_date) + "_" + str(uuid.uuid4()), filename.split('.')[-1])


class Image(models.Model):
    image = models.ImageField(
        validators=[FileExtensionValidator(['png', 'jpg'])], upload_to=image_path)
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
