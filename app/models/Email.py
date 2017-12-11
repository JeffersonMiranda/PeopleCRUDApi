from django.db import models
from app.models.Person import Person

class Email(models.Model):
    
    person = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='emails', blank = True)
    description = models.EmailField() ## EMAIL DESCRIPTION


