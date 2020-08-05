from django.urls import path

from .views import findRoute_view

urlpatterns = [
    path('', findRoute_view, name='findroute')
]