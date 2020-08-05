from django.shortcuts import render

from .forms import routeBetweenForm

def findRoute_view(request):

    routeForm = routeBetweenForm()

    context = {
        "page_title": 'Find Route',
        "home_isActive": 'active',
        "listOfStations": '',
        "about_isActive": '',
        "routeForm": routeForm,
    }

    return render(request, '../templates/routeform.html', context)
