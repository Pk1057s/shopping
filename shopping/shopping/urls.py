
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pr/", include("product.urls")),
    path("ac/", include('accounts.urls')),
    path("md/", include('modeling.urls')),
]
