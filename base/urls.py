from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create-photo/", views.PhotoCreationView.as_view(), name="create-photo"),
    path(
        "photo-detail/<int:pk>/<slug:slug>/",
        views.PhotoDetailView.as_view(),
        name="photo-detail",
    ),
]
