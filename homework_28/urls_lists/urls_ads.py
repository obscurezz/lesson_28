from django.urls import path

from ads.views import AdsListView, AdsDetailView, AdsCreateView, AdsDeleteView, AdsUpdateView, AdsImageView

urlpatterns = [
    path('ads/', AdsListView.as_view()),
    path('ads/<int:pk>/', AdsDetailView.as_view()),
    path('ads/create/', AdsCreateView.as_view()),
    path('ads/<int:pk>/update/', AdsUpdateView.as_view()),
    path('ads/<int:pk>/delete/', AdsDeleteView.as_view()),
    path('ads/<int:pk>/image/', AdsImageView.as_view()),
]
