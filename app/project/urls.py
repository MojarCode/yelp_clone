from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path("backend/api/", include("project.api.urls", namespace="api")),
]
