from django.urls import path

from ads.views import LocationsListView, LocationsDetailView, LocationsCreateView, LocationsDeleteView, LocationsUpdateView

urlpatterns = [
    path('locations/', LocationsListView.as_view()),
    path('locations/<int:pk>/', LocationsDetailView.as_view()),
    path('locations/create/', LocationsCreateView.as_view()),
    path('locations/<int:pk>/update/', LocationsUpdateView.as_view()),
    path('locations/<int:pk>/delete/', LocationsDeleteView.as_view()),
]
