from django.shortcuts import render
from .models import *


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
