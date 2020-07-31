from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Animal, Breed, LostPet


admin.site.site_header = 'Baytown Humane Society Admin Page'
admin.site.site_title = 'BHS'

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['id', 'breed']
    list_editable = ['breed']
    

@admin.register(Animal)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'breed']
    list_filter = ['breed']


@admin.register(LostPet)
class LostPetAdmin(admin.ModelAdmin):
    list_display = ['id', 'animal_name', 'image', 'description', 'breed']
    list_display_links = ['animal_name']
    list_filter = ['date_lost']
