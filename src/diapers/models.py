from django.db import models
from children.models import Child

# Create your models here.
class Diaper(models.Model):
    
    child = models.ForeignKey(Child)
    date = models.DateField()
    time = models.TimeField()
    
    diaper_choices = (
        ('Pee', 'Pee'),
        ('Poop', 'Poop'),
    )
    
    type = models.CharField(max_length=10, choices=diaper_choices,default='Pee')
    
    notes = models.CharField(max_length=200)
