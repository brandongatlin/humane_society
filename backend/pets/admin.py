from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Animal, Breed, LostPet, Human
from django.utils.html import format_html


admin.site.site_header = 'Baytown Humane Society Admin Page'
admin.site.site_title = 'BHS'

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['id', 'breed']
    list_editable = ['breed']
    

@admin.register(Animal)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'animal_name', 'photo', 'description', 'owner', 'breed', 'age']
    list_display_links = ['animal_name', 'photo']
    list_filter = ['breed']

    def photo(self,obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.image.url))


@admin.register(LostPet)
class LostPetAdmin(admin.ModelAdmin):
    list_display = ['id', 'animal_name', 'photo', 'description', 'breed', 'date_lost']
    list_display_links = ['animal_name', 'photo']
    list_filter = ['date_lost']

    def photo(self,obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.image.url))

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['first_name', 'last_name']
