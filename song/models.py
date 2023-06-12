from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=150, null=False)
    artists = models.ManyToManyField('artist.Artist', related_name='song')
    duration = models.CharField(null=False, max_length=10, default='00:00')
    category = models.ManyToManyField('category.Category', related_name='song')
    picURL = models.CharField(max_length=150, default="")
    def __str__(self):
        return self.title
