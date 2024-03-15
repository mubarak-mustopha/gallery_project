from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from .forms import PhotoModelForm
from .utils import get_month
from .models import Photo

# Create your views here.


class PaginatePhotoModelMixin:
    def get_context_data(self, page, per_page=8, queryset=Photo.objects.all()):
        # paginator
        paginator = Paginator(queryset, per_page)
        num_pages = paginator.num_pages
        page_range = paginator.page_range
        # requested page
        if int(page) not in page_range:
            page = num_pages
        current_page = paginator.get_page(page)
        # [(photo_obj,month)]
        photos_months_list = [
            (photo, get_month(photo.created.month)) for photo in current_page
        ]
        context = {
            "current_page": current_page,
            "page_num": int(page),
            "num_pages": num_pages,
            "page_range": page_range,
            "photos_months_list": photos_months_list,
        }

        return context


class HomeView(View, PaginatePhotoModelMixin):
    template_name = "home.html"
    photo_list = Photo.objects.all()

    def get(self, request):
        # requested page
        page = request.GET.get("page") or 1
        return render(
            request, self.template_name, context=self.get_context_data(page=page)
        )


@method_decorator(login_required(login_url="login"), name="dispatch")
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
        if request.user.is_authenticated:
            photo.views.add(request.user)
        return render(
            request, "photo_detail.html", {"photo": photo, "image_format": image_format}
        )


class UserPhotoList(View, PaginatePhotoModelMixin):
    def get(self, request, username):
        # get list of photos by username
        user = User.objects.get(username=username)
        user_photo_list = Photo.objects.filter(user=user)
        # requested page
        page = request.GET.get("page") or 1
        context = self.get_context_data(page=page, queryset=user_photo_list)
        context["heading_txt"] = f"Photos By {user.username}"

        return render(request, "photo-list.html", context)
