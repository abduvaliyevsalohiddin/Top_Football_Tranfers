from django.contrib import admin
from .models import *


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["nom", "davlat", "president", "coach", "yili"]
    search_fields = ["nom", "davlat__nom"]
    search_help_text = "Nom ustunlari bo'yicha qidiring"
    list_filter = ["davlat__nom"]


admin.site.register(Davlat)
# admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Transfer)
admin.site.register(HMavsum)
