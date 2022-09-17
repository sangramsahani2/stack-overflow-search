from django.db import models

class qustions(models.Model):
    tag = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    

# Create your models here.
