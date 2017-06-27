from django import forms

from .models import DisplayFlight

supported_airlines = ['AA', 'AC', 'AS', 'B6', 'CO', 'DL', 'F9', 'G4', 'HA', 'MQ', 'NK', 'OO', 'UA', 'VX', 'WN', 'FA']
AIRLINES = (
    ('AA', 'American Airlines'),
    ('AC', 'Air Canada'),
    ('AS', 'Alaska Airlines'),
    ('B6', 'JetBlue Airways'),
    ('CO', 'Continental Airlines'),
    ('DL', 'Delta Airlines'),
    ('F9', 'Frontier Airlines'),
    ('G4', 'Allegiant Air'),
    ('HA', 'Hawaiian Airlines'),
    ('MQ', 'Envoy Air'),
    ('NK', 'Spirit Airlines'),
    ('OO', 'SkyWest Airlines'),
    ('UA','United Airlines'),
    ('VX', 'Virgin America'),
    ('WN', 'SouthWest Airlines'),
    ('FA', 'Fake Test Airlines')
)

class SearchForm(forms.ModelForm):

    class Meta:
        model = DisplayFlight
        fields = ['unique_carrier', 'fl_num', 'origin', 'dest']


"""
class SearchForm(forms.Form):
        departure_code = forms.CharField(label='Departure Code', max_length=3)
        arrival_code = forms.CharField(label='Arrival Code', max_length=3)
        
        airline = forms.ChoiceField(choices=AIRLINES, required=True)
"""
