from django.db import models
from app.models.Person import Person

class Email(models.Model):
    
    person = models.ForeignKey(Person, on_delete = models.CASCADE, null = True, blank = True)
    description = models.EmailField() ## EMAIL DESCRIPTION


