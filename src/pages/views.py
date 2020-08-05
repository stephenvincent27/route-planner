from django.shortcuts import render

def homepage_view(request):

    context = {
        "page_title": 'Find Route',
        "home_isActive": 'active',
        "listOfStations": '',
        "about_isActive": '',
    }

    return render(request, '../templates/base.html', context)

def about_view(request):
    context = {
        "page_title": 'About',
        "home_isActive": '',
        "listOfStations": '',
        "about_isActive": 'active',
    }
    return render(request, '../templates/about.html', context)
