from django.http import HttpResponse
from django.shortcuts import render

from game.models import Character


def index(request):
    return HttpResponse('Welcome to Thaumatology!')


def characters(request):
    all_characters = Character.objects.all()
    context = {
        'characters': all_characters
    }
    return render(request, 'game/index.html', context)


def get_character(request, character_id):
    character = Character.objects.get(id=character_id)
    return HttpResponse(f'Showing character: {character}')
