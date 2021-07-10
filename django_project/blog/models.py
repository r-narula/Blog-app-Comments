from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# each class is a table in db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default='q')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    your_name = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=180)
    
    def __str__(self):
        return f"Comment by Name: {self.your_name}"