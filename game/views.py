from django.http import HttpResponse
from django.template import loader

from game.models import Character


def index(request):
    return HttpResponse('Welcome to Thaumatology!')


def characters(request):
    all_characters = Character.objects.all()
    template = loader.get_template('game/index.html')
    context = {
        'characters': all_characters
    }
    return HttpResponse(template.render(context, request))


def get_character(request, character_id):
    character = Character.objects.get(id=character_id)
    return HttpResponse(f'Showing character: {character}')
