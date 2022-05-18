from rest_framework import viewsets
from films.api import serializers
from films import models

class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FilmSerializer
    queryset = models.Film.objects.all()