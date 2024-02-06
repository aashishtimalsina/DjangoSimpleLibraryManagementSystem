from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class introduction(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.name