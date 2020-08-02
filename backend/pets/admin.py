from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Animal, Breed, Human
from django.utils.html import format_html


admin.site.site_header = 'Baytown Humane Society Admin Page'
admin.site.site_title = 'BHS'

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['id', 'breed_or_coat']
    list_editable = ['breed_or_coat']
    

@admin.register(Animal)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'animal_name', 'photo', 'description', 'owner', 'breed_or_coat', 'age']
    list_display_links = ['animal_name', 'photo']
    list_filter = ['breed_or_coat']

    def photo(self,obj):
        return format_html('<img src="{0}" style="width: 80px; height:80px;" />'.format(obj.image.url))


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['first_name', 'last_name']
