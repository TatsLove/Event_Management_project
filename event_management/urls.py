from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # root URL
    path("admin/", admin.site.urls),
    path("api/auth/", include("users.urls")),  # adjust if needed
    path("api/", include("events.urls")),      # adjust if needed
]
