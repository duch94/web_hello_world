from django.shortcuts import render
from django.http import HttpResponse
import urllib.request

# Create your views here.


def get_hero_matchups(hero_id):
    url = "https://api.opendota.com/api/heroes/" + str(hero_id) + "/matchups"
    hero_matchups = urllib.request.urlopen(url).read()
    return hero_matchups


def index(request):
    matchups_json = get_hero_matchups(1)
    return HttpResponse(matchups_json)