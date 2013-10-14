from django.db import models
from django.contrib.auth.models import User


class ChildManager(models.Manager):
      
    def add_child(self, fname, lname, mname ,gender, bdate,prnt):
        child = self.create(first_name=fname,last_name=lname,middle_name=mname,gender=gender,birth_date=bdate,parent=prnt)
        return child
        

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
    objects = ChildManager()
    
 
        
    


        
    