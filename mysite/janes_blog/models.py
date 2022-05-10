from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images')


class Comment(models.Model):
    post = models.ForeignKey('janes_blog.Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
