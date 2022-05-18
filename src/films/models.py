from django.db import models
from uuid import uuid4

class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    average = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)