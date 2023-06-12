from django.db import models

# Create your models here.

class LikedSong(models.Model):
    song = models.ManyToManyField('song.Song', related_name='LikedSong')
    user = models.ManyToManyField('authz.User', related_name='LikedSong')
