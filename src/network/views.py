from django.shortcuts import render

from .forms import routeBetweenForm

from .models import Station

def findRouteResult_view(request):

    context = {
        "page_title": 'Find Route: Result',
        "home_isActive": 'active',
        "listOfStations": '',
        "about_isActive": '',
    }

    return render(request, '../templates/routeformresult.html', context)

def findRoute_view(request):

    routeForm = routeBetweenForm(request.POST or None)
    msg = None
    msgType = None

    print(routeForm.is_valid())
    print(request.method)

    if routeForm.is_valid():
        return findRouteResult_view(request)
    elif request.POST:
        msg = 'Source and destination cannot be the same.'
        msgType = 'alert-danger'
        #routeForm = routeBetweenForm()

    #if(request.method == 'POST'):
    #    print("OK")
    #    routeForm = routeBetweenForm(request.POST)

        #src = request.POST['source']
        #dest = request.POST['destination']

        #print(src, dest)

        #if src == dest:
            #return forms.ValidationError("Source and destination cannot be the same.")

    #    if routeForm.is_valid():
    #        return findRouteResult_view(request)
    #    else:
    #        pass
    #else:
    #    routeForm = routeBetweenForm()

    #print("OK")

    context = {
        "page_title": 'Find Route',
        "home_isActive": 'active',
        "listOfStations": '',
        "about_isActive": '',
        "routeForm": routeForm,
        "message": msg,
        "message_type": msgType,
    }

    return render(request, '../templates/routeform.html', context)

def listOfStations_view(request):

    listOfStations = Station.objects.all().order_by('station_name')

    context = {
        "page_title": 'List Of Stations',
        "home_isActive": '',
        "listOfStations_isActive": 'active',
        "about_isActive": '',
        "listOfStations": listOfStations,
    }

    return render(request, '../templates/listofstations.html', context)
