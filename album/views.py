# Third Party Library
from django.views.generic import ListView

# Local Library
from .models import Photo

# Create your views here.


class PhotoListView(ListView):
    model = Photo
    template_engine = "album/photo_list.html"
    context_object_name = "photos"
