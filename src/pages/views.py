from django.shortcuts import render

def homepage_view(request):
    context = {
        "page_title": 'Home Page',
        "home_isActive": 'active',
        "about_isActive": '',
    }

    return render(request, '../templates/base.html', context)
