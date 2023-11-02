from django.shortcuts import render
from .models import *


def home(requests):
    return render(requests, "index.html")


def clubs(requests):
    return render(requests, "clubs.html")


def about(requests):
    return render(requests, "about.html")


def players(requests):
    content = {
        "players": Player.objects.all()
    }
    return render(requests, "players.html", content)
