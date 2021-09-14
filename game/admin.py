from django.contrib import admin

from .models import Character, Player, Round

admin.site.register(Character)
admin.site.register(Player)
admin.site.register(Round)
