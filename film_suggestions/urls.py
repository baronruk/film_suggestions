from django.contrib import admin
from django.urls import path

from .error_views import handler403, handler404, handler500  # noqa

urlpatterns = [
    path("admin/", admin.site.urls),
]
