from django.db import models
from app.models.Person import Person

class Address(models.Model):
    
    person = models.ForeignKey(Person, on_delete = models.CASCADE, null = True, blank = True)
    street = models.CharField(max_length = 50)
    postalCode = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)

