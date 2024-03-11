
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pr/", include("product.urls")),
    path("", include('accounts.urls')),
]
