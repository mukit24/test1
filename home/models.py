from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author=models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)