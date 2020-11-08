from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='collections', blank=True)
    owner_id = models.CharField(max_length=100, blank=True)
    is_disabled = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=100, blank=True)
    created_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name