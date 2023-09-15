from django.db import models

# Create your models here.
from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    logo = models.ImageField(upload_to="logo/%Y/%m/%d")
    
    def __str__(self):
        return str(self.name)