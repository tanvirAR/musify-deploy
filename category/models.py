from django.db import models

# Create your models here.

class Category(models.Model):
    name =   models.CharField(max_length=50, unique=True, null=False)
    color =  models.CharField(max_length=10, null=False)
    picURL = models.CharField(null=False, max_length=200)

    def __str__(self):
        return self.name
