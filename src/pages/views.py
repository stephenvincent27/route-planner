from django.shortcuts import render

def homepage_view(request):
    context = {
        "page_title": 'Find Route',
        "home_isActive": 'active',
        "about_isActive": '',
    }

    return render(request, '../templates/base.html', context)
