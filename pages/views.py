
# Create your views here.
# pages/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .loadout import drop, legend, primary, secondary
from.team_comp import playstation, xbox, pc

first= legend
second= primary
third= secondary
fourth= drop


def home(request):
    context= {
        "title": "Apex Random",
        "legend": first,
        "primary": second,
        "secondary": third,
        "drop": fourth,
    }
    return render(request, 'home.html', context)


lead= playstation 
follow= xbox
carry= pc

def about_page(request):
    context= {
        "title": "Apex Random",
        "playstation": lead,
        "xbox": follow,
        "pc": carry,
    }
    return render(request, 'about.html', context)





