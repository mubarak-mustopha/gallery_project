from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .models import Profile
from . import forms

# Create your views here.


class UserCreation(View):
    form_class = forms.UserRegistrationForm

    def get(self, request):
        return render(request, "registration/signup.html", {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            Profile.objects.create(user=user)
            return redirect("login")
        else:
            return render(request, "registration/signup.html", {"form": form})


class UserEditView(View):
    def get(self, request):
        user_edit_form = forms.UserEditForm(instance=request.user)
        profile_edit_form = forms.ProfileEditForm(instance=request.user.profile)
        return render(
            request,
            "registration/edit_profile.html",
            {"user_form": user_edit_form, "profile_form": profile_edit_form},
        )

    def post(self, request):
        user_edit_form = forms.UserEditForm(instance=request.user, data=request.POST)
        profile_edit_form = forms.ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )

        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            messages.success(request, message="Profile successfully updated.")
            return redirect("home")
        else:
            return render(
                request,
                "registration/edit_profile.html",
                {"user_form": user_edit_form, "profile_form": profile_edit_form},
            )


class UsersPageView(View):
    def get(self, request):
        profiles = Profile.objects.all()
        return render(request, "users.html", {"profiles": profiles})
