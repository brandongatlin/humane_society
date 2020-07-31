from django.db import models
from enum import Enum



class Breed(models.Model):
    breed = models.CharField(max_length=40)
    def __str__(self):
        return self.breed

class Animal(models.Model):
    animal_name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/', default='default.jpg', )
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)
    species = models.CharField(max_length=40)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.IntegerField() #months
    weight = models.IntegerField() #lbs
    height = models.IntegerField() #inches
    # available_to_foster = models.BooleanField()
    fixed = models.BooleanField()
    description = models.TextField()
    # adopted = models.DateTimeField()
    house_trained = models.BooleanField()

    created_at = models.DateTimeField(auto_now=True)

 

    def formatted_time(self):
        return self.created_at.strftime('%b %e %Y')


class LostPet(Animal):
    date_lost = models.DateTimeField()
    date_found = models.DateTimeField(default=None, blank=True, null=True)