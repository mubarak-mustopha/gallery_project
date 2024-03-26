from .models import Photo
from django.core.paginator import Paginator


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

        context = {
            "current_page": current_page,
            "page_num": int(page),
            "num_pages": num_pages,
            "page_range": page_range,
            "current_page": current_page,
        }

        return context
