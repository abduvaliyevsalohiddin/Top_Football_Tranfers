from django.shortcuts import render
from .models import *
from datetime import date


def home(requests):
    return render(requests, "index.html")


def clubs(requests):
    content = {
        "clubs": Club.objects.all()
    }
    return render(requests, "clubs.html", content)


def about(requests):
    return render(requests, "about.html")


def players(requests):
    content = {
        "players": Player.objects.all()
    }
    return render(requests, "players.html", content)


def stats(requests):
    return render(requests, "stats.html")


def transfers_records(requests):
    content = {
        "players": Transfer.objects.filter(narx__gt=50)[:100]
    }
    return render(requests, "transfer-records.html", content)


def players_U_20(requests):
    h_sana = str(date.today())  # "2023-11-03"
    yil = int(h_sana[:4]) - 20  # int("2023") - 20 = 2003
    yangi_sana = h_sana.replace(h_sana[:4], str(yil))  # "2003-11-03"

    content = {
        "players": Player.objects.filter(tugulgan_sana__gte=yangi_sana).order_by("-narx", "-tugulgan_sana"),
        "hozirgi_yil": int(date.today().year)
    }
    return render(requests, "U-20 players.html", content)


def davlat_clublari(request, davlat):
    content = {
        "clubs": Club.objects.filter(davlat__nom=davlat.capitalize())
    }
    return render(request, 'england.html', content)


def latest_transfers(request):
    content = {
        "players": Transfer.objects.filter(mavsum=HMavsum.objects.get(id=1))
    }
    return render(request, 'latest-transfers.html', content)


def country_clubs(request, club):
    content = {
        "players": Player.objects.filter(club__nom=club)
    }
    return render(request, 'country-clubs.html', content)
