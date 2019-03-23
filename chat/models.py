from django.db import models

class Support(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    key_words = models.TextField()
