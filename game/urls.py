from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters', views.characters, name='characters'),
    path('get_character/<int:character_id>', views.get_character, name='get_character'),
]
