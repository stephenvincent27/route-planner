"""route_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import homepage_view, about_view
from network.views import findRoute_view, findRouteResult_view, listOfStations_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('findroute/', findRouteResult_view),
    path('', findRoute_view),
    path('about/', about_view),
    path('listofstations/', listOfStations_view),
    #path('findroute/', findRoute_view),
]
