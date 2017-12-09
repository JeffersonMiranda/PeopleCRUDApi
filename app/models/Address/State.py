from django.db import models

class State(models.Model):
    
    code = models.CharField(max_length = 2, primary_key = True) 
    name = models.CharField(max_length = 50)
    


