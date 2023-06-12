from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(null=False, max_length=50)
    user = models.ManyToManyField('authz.User', related_name='Library')

    def __str__(self):
        return self.name




class LibrarySong(models.Model):
    library = models.ManyToManyField('Library', related_name='LibrarySong')
    song = models.ManyToManyField('song.Song', related_name='LibrarySong')
    user = models.ManyToManyField('authz.User', related_name='LibrarySong')
 
 