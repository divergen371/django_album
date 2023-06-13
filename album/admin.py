# Third Party Library
from django.contrib import admin

# Local Library
from .models import Photo, Tag

# Register your models here.


admin.site.register(Tag)
admin.site.register(Photo)
