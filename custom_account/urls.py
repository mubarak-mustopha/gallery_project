from django.urls import path
from django.contrib.auth import views as django_auth_views
from . import views as custom_views

urlpatterns = [
    path("login/", django_auth_views.LoginView.as_view(), name="login"),
    path("logout/", django_auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", custom_views.UserCreation.as_view(), name="signup"),
    path(
        "edit-profile/",
        custom_views.UserEditView.as_view(),
        name="edit-profile",
    ),
    path("users/", custom_views.UsersPageView.as_view(), name="users-page"),
]
