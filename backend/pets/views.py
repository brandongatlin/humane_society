from django.http import JsonResponse
from .models import Animal, LostPet


def all_pets(request):
    pets = Animal.objects.values()
    return JsonResponse({'data': list(pets)})

def single_pet(request, pet_id):
    pet_detail = Animal.objects.filter(id__exact=pet_id).values()[0]
    return JsonResponse({'data': pet_detail})

def all_lost(request):
    pets = LostPet.objects.values()
    return JsonResponse({'data': list(pets)})

def single_lost_pet(request, pet_id):
    pet_detail = LostPet.objects.filter(id__exact=pet_id).values()[0]
    return JsonResponse({'data': pet_detail})