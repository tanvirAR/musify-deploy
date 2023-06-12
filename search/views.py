from django.db.models import Q
from django.views import View
from django.http import JsonResponse
from artist.models import Artist
from song.models import Song

# Create your views here.


class SearchView(View):
    def get(self, request, query):
        query_list = query.split(",")

        artist_queries = [Q(name__icontains=term) for term in query_list]
        combined_artist_query = Q()

        for query in artist_queries:
            combined_artist_query |= query

        song_queries = [Q(title__icontains=term) for term in query_list]
        combined_song_query = Q()

        for query in song_queries:
            combined_song_query |= query

        artists = Artist.objects.filter(
            combined_artist_query).values('pk', 'name', 'imageURL')[:20]
        songs = Song.objects.filter(combined_song_query).values(
            'title', 'url', 'artists', 'duration', 'picURL', 'artists__name', 'id')[:20]

        return JsonResponse({"artists": list(artists), "songs": list(songs)})



# class Search(View):
#     def get(self, request):
#         songs = Song.objects.filter(picURL__icontains='ahtt').values(
#             'title', 'url', 'artists', 'duration', 'picURL', 'artists__name', 'id')
#         return JsonResponse({"data": list(songs)})
