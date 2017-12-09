from django.db import models
from app.models.Address.State import State
from app.models.Address.City import City
from app.models.Person import Person

class Address(models.Model):
    
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    street = models.CharField(max_length = 50)
    postalCode = models.CharField(max_length = 50)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    state = models.ForeignKey(State, on_delete = models.CASCADE)

