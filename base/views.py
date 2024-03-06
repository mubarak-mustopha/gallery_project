from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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


@method_decorator(login_required, name="dispatch")
class PhotoCreationView(View):

    def get(self, request):
        form = PhotoModelForm()
        return render(request, "create_photo.html", {"form": form})

    def post(self, request):
        form = PhotoModelForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.user = request.user
            photo.save()
            messages.success(request, message="Post successfully uploaded.")
            return redirect(photo)
        else:
            return render(request, "create_photo.html", {"form": form})


class PhotoDetailView(View):
    def get(self, request, pk, slug):
        photo = Photo.objects.get(id=pk, slug=slug)
        image_format = photo.image.name.rsplit(".")[-1].upper()
        return render(
            request, "photo_detail.html", {"photo": photo, "image_format": image_format}
        )
