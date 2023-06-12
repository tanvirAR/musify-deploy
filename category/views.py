from django.views import View
from django.http import JsonResponse

from json import loads

from .models import Category
from song.models import Song
from artist.models import Artist

import random

# Create your views here.

# get all the categories from DB
class CategoryView(View):
    def get(self, request):
        try:
            data = Category.objects.all().values('pk', 'name', 'color', 'picURL')
            return JsonResponse({"data": list(data)}, safe=True)
        except Exception as error:
            return JsonResponse({"message": str(error)}, safe=False)
        
    
class SingleCategory(View):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
            data = {
                "pk": category.pk,
                "name": category.name,
                "color": category.color,
                "picURL": category.picURL,
            }
            return JsonResponse({"data": data}, safe=True)
        except Exception as error:
            return JsonResponse({"message": str(error)}, safe=False)


class SingleCategorySongView(View):
    def get(self, request, category_id):
        try:
            artists = Song.objects.select_related(
                'artists').filter(category__pk=category_id)
            songs = artists.values('title', 'url', 'duration',
                                   'picURL', 'artists__name', 'artists', 'id', 'artists__imageURL')
            # artists_data = artists.values(
            #     'artists__name', 'artists',  'artists__imageURL')
            # return JsonResponse({"songs": list(songs), "artists": list(artists_data)})
            return JsonResponse({"songs": list(songs)})
        except Exception as error:
            return JsonResponse({"error": str(error)}, safe=False)




class SingleRandomCategory(View):
    def get(relf, request):
        try:
            categories = list(Category.objects.all().values('id', 'name'))
            random_category = random.choice(categories)
            
            artists = Song.objects.select_related(
                'artists').filter(category__pk=random_category['id'])[:8]
            songs = artists.values('title', 'url', 'duration',
                                   'picURL', 'artists__name', 'artists', 'id')
            
            return JsonResponse({"category": random_category, "categoryData": list(songs)}, status=200)

        except Exception as error:
            return JsonResponse({"error": str(error)}, safe=False, status=400)
