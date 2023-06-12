from django.views import View
from django.http import JsonResponse
from random import sample

from .models import Song


# Create your views here.

class SongView(View):
    def get(self, request, song_id):
        try:
            data = Song.objects.filter(pk=song_id).values(
                'title', 'url', 'duration', 'picURL', 'artists__name', 'artists', 'id')
            return JsonResponse({"data": list(data)[0]})

        except Exception as error:
            return JsonResponse({"message": str(error)})


# get N number of random songs. N passed by query parameter
class RandomSongs(View):
    def get(self, request, number_of_songs):
        try:
            random_songs = sample(list(Song.objects.all().values(
                'title', 'url', 'duration', 'picURL', 'artists__name', 'artists', 'id')), int(number_of_songs))
            return JsonResponse({"data": random_songs}, status=200)

        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)


# get songs list by given array of ids in query parameter 
class MultipleSongsView(View):
    def get(self, request):
        try:
            ids_list = request.GET.getlist('ids[]', [])
            ids_int = [int(numeric_string) for numeric_string in ids_list]
            songs = Song.objects.filter(pk__in=ids_int).values(
                'title', 'url', 'duration', 'picURL', 'artists__name', 'artists', 'id')
            return JsonResponse({"data": list(songs)})

        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)
        
