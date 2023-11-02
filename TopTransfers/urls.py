from django.contrib import admin
from django.urls import path

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('clubs/', clubs),
    path('about/', about),
    path('players/', players),
    path('stats/', stats),
    path('transfers_records/', transfers_records),
]
