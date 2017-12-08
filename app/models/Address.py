from django.db import models

class Address(models.Model):
    
    street = models.CharField(max_length = 50)
    postalCode = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)

