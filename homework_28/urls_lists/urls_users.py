from django.urls import path

from ads.views import UsersListView, UsersDetailView, UsersCreateView, UsersDeleteView, UsersUpdateView

urlpatterns = [
    path('users/', UsersListView.as_view()),
    path('users/<int:pk>/', UsersDetailView.as_view()),
    path('users/create/', UsersCreateView.as_view()),
    path('users/<int:pk>/update/', UsersUpdateView.as_view()),
    path('users/<int:pk>/delete/', UsersDeleteView.as_view()),
]
