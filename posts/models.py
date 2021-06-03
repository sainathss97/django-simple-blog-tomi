from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    titles = models.CharField(max_length=200)
    body = models.CharField(max_length=500000)
    created_at  = models.DateTimeField( default = datetime.now  ,  blank = True)