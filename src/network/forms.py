from django import forms

from .models import Station

class routeBetweenForm(forms.Form):
    
    allStations     = Station.objects.all().order_by('station_name')
    allStationsList = [(index, allStations[index]) for index in range(len(allStations))]

    source          = forms.ChoiceField(choices=allStationsList)
    destination     = forms.ChoiceField(choices=allStationsList)