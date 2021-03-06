from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("website.urls")),
    path("accounts/", include("accounts.urls")),
    path("bank/", include("bank.urls")),
    path("admin-app/", admin.site.urls),
]
