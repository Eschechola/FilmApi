from rest_framework import serializers
from films import models

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Film
        fields = '__all__'