from django.db import models
from datetime import datetime


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=20000)
    date_posted = models.DateField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog_images/', blank=True)

    def __str__(self):
        return self.title
