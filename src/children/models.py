from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Child(models.Model):
    parent = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1,choices=gender_choices,default='F')
    birth_date = models.DateTimeField('Birth Date')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.first_name
    