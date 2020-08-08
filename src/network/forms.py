from django import forms

from .models import Station

allStations     = Station.objects.all().order_by('station_name')
allStationsList = [(index, allStations[index]) for index in range(len(allStations))]

class routeBetweenForm(forms.Form):

    source          = forms.ChoiceField(choices=allStationsList)
    destination     = forms.ChoiceField(choices=allStationsList)

    def clean(self):

        src = self.cleaned_data['source']
        dest = self.cleaned_data['destination']

        if(src == dest):
            raise forms.ValidationError("Source and destination cannot be the same.")

        return self.cleaned_data
