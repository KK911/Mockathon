from django.db import models
from datetime import date


# Create your models here.
class SampleUser(models.Model):
        
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dob = models.DateField(verbose_name='Date of birth')    
    email = models.CharField(max_length=200)
    
    def age(self):
        today = date.today()
        try: 
            birthday = self.dob.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = self.dob.replace(year=today.year, day=self.dob.day-1)
        if birthday > today:
            return today.year - self.dob.year - 1
        else:
            return today.year - self.dob.year