from django.contrib import admin
from django.urls import path, include

# ALl urls for my site
urlpatterns = [path("admin/", admin.site.urls),
               path("", include("Users.urls"))]
