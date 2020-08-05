from django import forms

from .models import Station

class routeBetweenForm(forms.Form):
    allStations = Station.objects.all()