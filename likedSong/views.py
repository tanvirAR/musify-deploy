from django.views import View
from django.http import JsonResponse
from json import loads

from authz.models import User
from song.models import Song
from .models import LikedSong

# Create your views here.

class LikedSongView(View):
    def get_user(self, request):
        userData = request.session.get("user")
        return User.objects.filter(email=userData['email']).first()
    

    def post(self, request):
        try:
            user = self.get_user(request)
            req_data = loads(request.body)
            song_to_add = Song.objects.get(pk=req_data.get('songId'))
            new_liked_song = LikedSong()
            new_liked_song.save()
            new_liked_song.user.set([user])
            new_liked_song.song.set([song_to_add])
            return JsonResponse({"message": "LikedSong created successfully."})

        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)


    def get(self, request):
        try:
            user = self.get_user(request)
            data = LikedSong.objects.filter(user=user).values(
                'song__title', 'song__url', 'song__duration', 'song__picURL', 'song__artists__name', 'song__artists', 'song__id', 'id')
            return JsonResponse({"data": list(data)})
        except Exception as error:
           return JsonResponse({"message": str(error)}, status=400)
        


        

    

class SingleLikedSongViewClass(View):
    def get_user(self, request):
        userData = request.session.get("user")
        return User.objects.filter(email=userData['email']).first()
    
    # check song by song - id if it is liked song for this user or not 
    def get(self, request, trackId):
        try:
            user = self.get_user(request)
            data = LikedSong.objects.filter(user=user, song__id=trackId)
            if (data):
                return JsonResponse({"isLiked": True}, status=200)
            else:
                return JsonResponse({"isLiked": False}, status=200)
        except Exception as error:
           return JsonResponse({"message": str(error)}, status=400)


    # remove song by song id from liked song model 
    def post(self, request):
        try:
            user = self.get_user(request)
            data = loads(request.body)
            print(data)
            liked_song = LikedSong.objects.get(user=user, song__id=data['id'])
            liked_song.delete()
            return JsonResponse({"message": "LikedSong removed successfully!"})

        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)