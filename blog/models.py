from distutils.command.upload import upload
from re import T
from tabnanny import verbose
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, unique=True)
    images = models.ImageField(upload_to='img/post')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'

    def publish(self):
        self.published = True
        self.publish_date = timezone.now()
        self.save()
    
    def get_absolute_url(self):
        return reverse('single_post', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
