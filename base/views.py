from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from .forms import PhotoModelForm
from .models import Photo

# Create your views here.


class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)


class PhotoCreationView(View):

    def get(self, request):
        form = PhotoModelForm()
        return render(request, "create_photo.html", {"form": form})

    def post(self, request):
        form = PhotoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message="Post successfully uploaded.")
            return redirect("home")
        else:
            print(form.errors)
            return HttpResponse("Invalid form")
