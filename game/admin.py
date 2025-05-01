from django.contrib import admin
from .models import Game, Winner

class WinnerInLine(admin.TabularInline):
    """ To view winners through admin """
    model = Winner
    extra = 1

@admin.register(Game)
class GamelistAdmin(admin.ModelAdmin):
    """ To add or edit songs directly from admin """
    inlines = [WinnerInLine]