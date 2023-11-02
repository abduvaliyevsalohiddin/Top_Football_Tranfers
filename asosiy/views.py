from django.shortcuts import render


def home(requests):
    return render(requests, "index.html")


def clubs(requests):
    return render(requests, "clubs.html")


def about(requests):
    return render(requests, "about.html")
