from django.contrib import admin
from .models import Animal, Breed, LostPet


class BreedAdmin(admin.ModelAdmin):
    list_display = ['id', 'breed']

class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'breed']

class LostPetAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'breed']




admin.site.register(Breed, BreedAdmin)
admin.site.register(Animal, PetAdmin)
admin.site.register(LostPet, LostPetAdmin)
