from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('clubs/', clubs),
    path('about/', about),
    path('players/', players),
    path('stats/', stats),
    path('transfers_records/', transfers_records),
    path('players_U_20/', players_U_20),
    path('countries/<str:davlat>/', davlat_clublari),
    path('latest_transfers/', latest_transfers),

    path('transfers_archive/', transfers_archive),

    path('country_clubs/<str:club>/', country_clubs),
    path('season_transfers/<str:m>/', season_transfers),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
