from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField('Category', related_name='events')
    host = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Account(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()