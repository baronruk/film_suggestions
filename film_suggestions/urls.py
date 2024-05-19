from django.contrib import admin
from django.urls import path

from . import views
from .error_views import handler403, handler404, handler500  # noqa

urlpatterns = [
    path("", views.landing, name="landing"),
    path("admin/", admin.site.urls),
]
