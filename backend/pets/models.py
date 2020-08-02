from django.db import models
from datetime import datetime as dt
import pytz
from colorfield.fields import ColorField

class Human(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def name(self):
        return f'{self.first_name} {self.last_name}'


class Breed(models.Model):
    breed = models.CharField(max_length=40)
    def __str__(self):
        return self.breed


class Animal(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    animal_name = models.CharField(max_length=40)
    owner = models.ForeignKey(Human, on_delete=models.CASCADE, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='images/default.png' )
    primary_color = ColorField(default='#FF0000')
    secondary_color = ColorField(default='#FF0000')
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)
    species = models.CharField(max_length=40)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, default=None, blank=True, null=True)
    birth_date = models.DateTimeField(default=None, blank=True, null=True)
    weight = models.IntegerField() #lbs
    height = models.IntegerField() #inches
    fixed = models.BooleanField()
    description = models.TextField()
    adopted = models.DateTimeField(default=None, blank=True, null=True)
    house_trained = models.BooleanField()
    micro_chipped = models.BooleanField(default=False)
    euthanized = models.DateTimeField(default=None, blank=True, null=True)
    reason_euthanized = models.TextField(default=None, blank=True, null=True)
 
    def __str__(self):
        return self.animal_name

    def formatted_time(self):
        return self.created_at.strftime('%b %e %Y')

    def age(self):
        dif =  dt.now(tz=pytz.utc) - self.birth_date
        years = dif.days // 365
        months = (dif.days % 365) // 30
        return f'{years} years and {months} months'



class LostPet(Animal):
    date_lost = models.DateTimeField()
    date_found = models.DateTimeField(default=None, blank=True, null=True)