from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    city=models.CharField(max_length=200)



