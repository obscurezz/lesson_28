from django.urls import path

from ads.views import CategoriesListView, CategoriesDetailView, CategoriesCreateView, CategoriesDeleteView, CategoriesUpdateView

urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('categories/<int:pk>/', CategoriesDetailView.as_view()),
    path('categories/create/', CategoriesCreateView.as_view()),
    path('categories/<int:pk>/update/', CategoriesUpdateView.as_view()),
    path('categories/<int:pk>/delete/', CategoriesDeleteView.as_view()),
]
