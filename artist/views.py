from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from random import sample

from .models import Artist
from song.models import Song


# Create your views here.


class ArtistView(View):
    def get(self, request, artist_id):
        try:
            data = Artist.objects.filter(
                pk=artist_id).values('name', 'imageURL')

            return JsonResponse({"data": list(data)}, safe=False)

        except Exception as error:
            return JsonResponse({"message": str(error)})


class RandomArtistsView(View):
    def get(self, request, number):
        try:
            random_artists = sample(list(Artist.objects.all()), int(number))
            artist_list = []
            for artist in random_artists:
                artist_dict = {
                    "id": artist.pk,
                    "name": artist.name,
                    "imageURL": artist.imageURL
                }
                artist_list.append(artist_dict)
            return JsonResponse({"data": artist_list}, safe=False)
        except Exception as error:
            return JsonResponse({"message": str(error)})


class ArtistSongView(View):
    def get(self, request, artist_id):
        try:
            data = Song.objects.filter(artists__pk=artist_id).values(
                'title', 'url', 'duration', 'picURL', 'artists__name', 'artists', 'id')

            return JsonResponse({"data": list(data)}, safe=False)

        except Exception as error:
            return JsonResponse({"message": str(error)})


class MultipleArtistsView(View):
    def get(self, request):
        try:
            ids_list = request.GET.getlist('ids[]', [])
            ids_int = [int(numeric_string) for numeric_string in ids_list]
            artists = Artist.objects.filter(pk__in=ids_int).values()
            return JsonResponse({"data": list(artists)})

        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)
