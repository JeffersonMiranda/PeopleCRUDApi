from django.db import models
from app.models.Person import Person

class PhoneNumber(models.Model):
    
    person = models.ForeignKey(Person, on_delete = models.CASCADE, null = True, blank = True)
    number = models.CharField(max_length = 50)



