from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from .forms import PhotoModelForm
from .models import Photo

# Create your views here.


class HomeView(View):
    template_name = "home.html"
    photo_list = Photo.objects.all()

    def get(self, request):
        page = request.GET.get("page") or 1
        paginator = Paginator(self.photo_list, 8)
        num_pages = paginator.num_pages
        current_page = paginator.get_page(page)
        context = {
            "current_page": current_page,
            "page_num": int(page),
            "num_pages": num_pages,
            "ind": range(1, num_pages + 1),
        }
        return render(request, self.template_name, context=context)


@method_decorator(login_required, name="dispatch")
class PhotoCreationView(View):

    def get(self, request):
        form = PhotoModelForm()
        return render(request, "create_photo.html", {"form": form})

    def post(self, request):
        form = PhotoModelForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
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
