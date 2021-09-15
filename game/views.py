from django.http import HttpResponse

from game.models import Character


def index(request):
    return HttpResponse('Welcome to Thaumatology!')


def characters(request):
    all_characters = ', '.join([c.type for c in Character.objects.all()])
    return HttpResponse(f'{all_characters}')


def get_character(request, character_id):
    character = Character.objects.get(id=character_id)
    return HttpResponse(f'Showing character: {character}')
