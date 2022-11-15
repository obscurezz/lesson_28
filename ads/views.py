import json

from django.db import IntegrityError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from ads.base_views import BaseListView, BaseDetailView, BaseCreateView, BaseDeleteView, BaseUpdateView
from ads.models import Ad, Category, Location, User


# block of full lists
class AdsListView(BaseListView):
    model = Ad
    ordering_field = "price"


class CategoriesListView(BaseListView):
    model = Category


class LocationsListView(BaseListView):
    model = Location


class UsersListView(BaseListView):
    model = User
    ordering_field = "username"


# block of detail view of exact object
class AdsDetailView(BaseDetailView):
    model = Ad
    ordering_field = "price"
    fk_fields = ["author", "category"]

    def get(self, *args, **kwargs):
        data = get_object_or_404(self.model.objects.select_related(*self.fk_fields))
        result_data = model_to_dict(data)
        result_data['image'] = data.get_image_url

        return JsonResponse(result_data)


class CategoriesDetailView(BaseDetailView):
    model = Category


class LocationsDetailView(BaseDetailView):
    model = Location


class UsersDetailView(BaseDetailView):
    model = User
    ordering_field = "username"
    fk_fields = ["location"]


# block of insert views
@method_decorator(csrf_exempt, name='dispatch')
class AdsCreateView(BaseCreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        data_object = self.model.objects.create(**data)
        data_object.author = get_object_or_404(User, pk=data.get('author_id'))
        data_object.category = get_object_or_404(Category, pk=data.get('category_id'))

        return JsonResponse(model_to_dict(data_object))


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesCreateView(BaseCreateView):
    model = Category
    fields = ['name']


@method_decorator(csrf_exempt, name='dispatch')
class LocationsCreateView(BaseCreateView):
    model = Location
    fields = ['name', 'lat', 'lng']


@method_decorator(csrf_exempt, name='dispatch')
class UsersCreateView(BaseCreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'role', 'password', 'age', 'location']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        data_object = self.model.objects.create(**data)
        try:
            data_object.location = get_object_or_404(Location, pk=data.get('location_id'))
        except IntegrityError:
            data_object.location = Location.objects.get_or_create(name=data.get('location'))

        return JsonResponse(model_to_dict(data_object))


# block of delete views
@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(BaseDeleteView):
    model = Ad


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesDeleteView(BaseDeleteView):
    model = Category


@method_decorator(csrf_exempt, name='dispatch')
class LocationsDeleteView(BaseDeleteView):
    model = Location


@method_decorator(csrf_exempt, name='dispatch')
class UsersDeleteView(BaseDeleteView):
    model = User


# block of update views
@method_decorator(csrf_exempt, name='dispatch')
class AdsUpdateView(BaseUpdateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesUpdateView(BaseUpdateView):
    model = Category
    fields = ['name']


@method_decorator(csrf_exempt, name='dispatch')
class LocationsUpdateView(BaseUpdateView):
    model = Location
    fields = ['name', 'lat', 'lng']


@method_decorator(csrf_exempt, name='dispatch')
class UsersUpdateView(BaseUpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'role', 'password', 'age', 'location']


# image view for Ads
@method_decorator(csrf_exempt, name='dispatch')
class AdsImageView(UpdateView):
    model = Ad
    fields = ['name', 'image']

    def post(self, request, *args, **kwargs):
        data = self.get_object()
        data.image = request.FILES['image']
        data.save()

        return JsonResponse({'status': 'image uploaded'})
