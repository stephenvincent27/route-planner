from django import forms

from .models import Station

allStations     = Station.objects.all().order_by('station_name')
allStationsList = [(index, allStations[index]) for index in range(len(allStations))]

class routeBetweenForm(forms.Form):

    source          = forms.ChoiceField(choices=allStationsList)
    destination     = forms.ChoiceField(choices=allStationsList)
