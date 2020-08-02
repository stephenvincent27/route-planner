from django.shortcuts import render

def homepage_view(request):
    context = {
        "page_title": 'Home Page',
    }

    return render(request, '../templates/base.html', context)
