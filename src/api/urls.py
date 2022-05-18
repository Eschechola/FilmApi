from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers;

from films.api import viewsets as filmsviewsets

route = routers.DefaultRouter()

route.register(r'films', filmsviewsets.FilmViewSet, basename="Films")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
