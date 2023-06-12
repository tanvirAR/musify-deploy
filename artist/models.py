from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100, null=False)
    imageURL = models.CharField(max_length=100, default="")
    
    

    def __str__(self):
        return self.name
