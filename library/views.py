from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from json import loads
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Library, LibrarySong
from authz.models import User
from song.models import Song
from django.views.generic import TemplateView
from django.core import serializers

# Create your views here.
class LibraryView(View):
    def get_user(self, request):
        userData = request.session.get("user")
        if not userData:
            return False
        return User.objects.filter(email=userData['email']).first()

    def get(self, request):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            libraries = Library.objects.filter(user=user).values('pk', 'name')
            return JsonResponse({"data": list(libraries)}, status=200)
        except Exception as error:
            # print(error.message)
            return JsonResponse({"message": str(error)}, safe=False, status=400)

    def delete(self, request):
        try:
            user = self.get_user(request)
            data = loads(request.body)
            print(data.get('id'))
            Library.objects.filter(user=user, pk=data.get('id')).delete()
            return JsonResponse({"message": "Library deleted successfully!"})
        except Exception as error:
            return JsonResponse({"message": str(error)}, safe=False, status=400)

    def put(self, request):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            data = loads(request.body)
            library = get_object_or_404(Library, user=user, pk=data.get('id'))
            library.name = data.get('name')
            library.save()
            return JsonResponse({"message": "Library updated successfully!"})
        except Http404:
            return JsonResponse({"message": "Library not found for user!"}, status=404)
        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)




class LibrarySingleView(View):
    def get_user(self, request):
        userData = request.session.get("user")
        if not userData:
            return False
        return User.objects.filter(email=userData['email']).first()
    
    def get(self, request, lib_id):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            single_library = Library.objects.get(user=user, pk=int(lib_id))
            return JsonResponse({"data": {
        "id": single_library.pk,
        "name": single_library.name,
    }}, status=200)
        except Exception as error:
            # print(error.message)
            return JsonResponse({"message": str(error)}, safe=False, status=400)




class LibraryCreateView(View):
    def post(self, request):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            data = loads(request.body)
            newLib = Library(name=data.get('name'))
            newLib.save()
            newLib.user.set([user])
            return JsonResponse({"library": {"pk": newLib.pk, "name": newLib.name}})
        except ValidationError as error:
            JsonResponse({"message": "Error occured!"}, status=400)

    def get_user(self, request):
        userData = request.session.get("user")
        if not userData:
            return False
        return User.objects.filter(email=userData['email']).first()






class LibrarySongView(View):
    def get_user(self, request):
        userData = request.session.get("user")
        if not userData:
            return False
        return User.objects.filter(email=userData['email']).first()


    def post(self, request):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            data = loads(request.body)
            song_to_add = get_object_or_404(Song, pk=data.get('songId'))
            lib_to_add = get_object_or_404(Library, pk=data.get('libId'))
            newLibSong = LibrarySong()
            newLibSong.save()
            newLibSong.user.set([user])
            newLibSong.song.set([song_to_add])
            newLibSong.library.set([lib_to_add])
            return JsonResponse({"message": "Song successfully added to library!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        


    def get(self, request, lib_id=None):
        if lib_id:
            try:
                user = self.get_user(request)
                if not user:
                    return JsonResponse({"user": "Authenntication error"}, status=400)
                data = LibrarySong.objects.filter(user=user, library__pk=int(lib_id)).values('id', 'song__title', 'song__url', 'song__artists', 'song__duration', 'song__picURL', 'song__artists__name', 'song__id')
                return JsonResponse({"data": list(data)})

            except Exception as error:
                return JsonResponse({"message": str(error)}, status=400)
        
        else: 
            return JsonResponse({"message": "Library id is required  as a param"}, status=400)



    def delete(self, request):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            data = loads(request.body)
            LibrarySong.objects.filter(user=user, pk=data.get('id')).delete()
            return JsonResponse({"message": "Library deleted successfully!"})
        
        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)



# create a library and add a song

class LibraryCreateAndAddSongView(View):
    def get_user(self, request):
        userData = request.session.get("user")
        if not userData:
            return False
        return User.objects.filter(email=userData['email']).first()



    def post(self, request):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            data = loads(request.body)
            newLib = Library(name=data.get('libraryName'))
            newLib.save()
            newLib.user.set([user])

            song_to_add = get_object_or_404(Song, pk=data.get('songId'))
            newLibSong = LibrarySong()
            newLibSong.save()
            newLibSong.user.set([user])
            newLibSong.song.set([song_to_add])
            newLibSong.library.set([newLib])

            
            return JsonResponse({"library": {"pk": newLib.pk, "name": newLib.name}})
        except ValidationError as error:
            JsonResponse({"message": "Error occured!"}, status=400)



class SearchLibraryView(View):
    def get_user(self, request):
        userData = request.session.get("user")
        if not userData:
            return False
        return User.objects.filter(email=userData['email']).first()


    def get(self, request, search_query):
        try:
            user = self.get_user(request)
            if not user:
                return JsonResponse({"user": "Authenntication error"}, status=400)
            libraries = Library.objects.filter(user=user, name__icontains=search_query).values('pk', 'name')
            return JsonResponse({"data": list(libraries)}, status=200)
        except Exception as error:
            # print(error.message)
            return JsonResponse({"message": str(error)}, safe=False, status=400)
