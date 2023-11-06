from django.contrib import admin
from .models import *


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "davlat", "president", "coach", "yili"]
    search_fields = ["nom", "davlat__nom"]
    search_help_text = "Nom, Davlat ustunlari bo'yicha qidiring"
    list_filter = ["davlat__nom"]
    ordering = ["id"]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "davlat", "tugulgan_sana", "narx", "club", "pozitsiya"]
    search_fields = ["ism", "davlat__nom", "club__nom"]
    search_help_text = "Ism, Davlat va Club ustunlari bo'yicha qidiring"
    list_filter = ["club"]
    autocomplete_fields = ["club"]
    ordering = ["id"]


admin.site.register(Davlat)
# admin.site.register(Club)
# admin.site.register(Player)
admin.site.register(Transfer)
admin.site.register(HMavsum)
