from django.db import models
from site_app.models import Collection

class Unit(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)
    image = models.ImageField(upload_to='units')
    is_disabled = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name