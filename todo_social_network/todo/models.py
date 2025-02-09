from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    deadline = models.DateField(blank=True,null=True)
    text = models.CharField(max_length=120)
    likes = models.IntegerField(default=0)
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    text = models.TextField(blank=False,null=False)
    date_create = models.DateField(auto_now=True)


