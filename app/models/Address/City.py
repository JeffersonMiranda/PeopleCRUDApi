from django.db import models
from app.models.Address.State import State

class City(models.Model):
    
    state_code = models.ForeignKey(State, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

