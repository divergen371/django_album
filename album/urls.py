# Third Party Library
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Local Library
from .views import PhotoListView

urlpatterns = [
    path("", PhotoListView.as_view(), name="photo-list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
