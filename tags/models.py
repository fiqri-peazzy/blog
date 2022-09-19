from django.db import models
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def get_url(self):
        return reverse('tag_post', args=[self.slug])

    def __str__(self):
        return self.tag_name
