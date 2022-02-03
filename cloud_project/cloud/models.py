from django.db import models

class Name(models.Model):
    name = models.TextField(max_length=100)
