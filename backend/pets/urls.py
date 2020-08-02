from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_pets, name="allPets"),
    path('<int:pet_id>/', views.single_pet, name='pet_detail'),
    path('lost/', views.all_lost, name="allLost"),
    path('lost/<int:pet_id>/', views.single_lost_pet, name='lost_pet_detail'),
]