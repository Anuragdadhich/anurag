from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=255)
    lsname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)