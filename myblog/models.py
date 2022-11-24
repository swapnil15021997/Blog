from django.urls import reverse
from django.utils import timezone
from unittest import mock
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish') 

class Post(models.Model):
    STATUS_CHOICE = (('draft','Draft'),('publish','Publish'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    author =models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='Posts' )
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE, default='draft')
    objects=CustomManager()

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug]) 
       

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name= models.CharField(max_length=32)
    email = models.EmailField()
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering=('created',)
    def __str__(self):
        return "Commented By{} on {}".format(self.name,self.post)
