import json

from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from ads.models import BaseModel
from homework_28.settings import TOTAL_ON_PAGE


class BaseListView(ListView):
    model: BaseModel = BaseModel
    ordering_field: str = "name"

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list: QuerySet = self.object_list.order_by(self.ordering_field)
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)

        resulted_objects: list[dict] = [{'id': position.id, self.ordering_field: getattr(position, self.ordering_field)}
                                        for position in page_object]
        response = {
            'objects': resulted_objects,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }

        return JsonResponse(response)


class BaseDetailView(DetailView):
    model: BaseModel = BaseModel
    fk_fields: list = None

    def get(self, *args, **kwargs):
        data = get_object_or_404(self.model.objects.select_related(*self.fk_fields))

        return JsonResponse(model_to_dict(data))


class BaseCreateView(CreateView):
    model: BaseModel = BaseModel
    fields: list = []

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        data_object = self.model.objects.create(**data)

        return JsonResponse(model_to_dict(data_object))


class BaseDeleteView(DeleteView):
    model: BaseModel = BaseModel
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'deleted'})


class BaseUpdateView(UpdateView):
    model: BaseModel = BaseModel
    fields = []

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)

        data_object = self.object
        data_object.__dict__.update(data)
        data_object.save()

        return JsonResponse({'status': 'updated'})
