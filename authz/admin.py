from django.contrib import admin
from authz.models import User
from category.models import Category
from song.models import Song
from artist.models import Artist
from likedSong.models import LikedSong
from library.models import Library, LibrarySong
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(LikedSong)
class LikedSongAdmin(admin.ModelAdmin):
    pass


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass


@admin.register(LibrarySong)
class LibrarySongAdmin(admin.ModelAdmin):
    pass
