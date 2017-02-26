from django import forms

supported_airlines = ['UA', 'AA', 'NK', 'B6', 'WN', 'VX', 'F9', 'CO', 'AS', 'DL']
AIRLINES = (
    ('UA','United Airlines'),
    ('AA', 'American Airlines'),
    ('NK', 'Spirit Airlines'),
    ('B6', 'JetBlue Airways'),
    ('WN', 'SouthWest Airlines'),
    ('VN', 'Virgin America'),
    ('F9', 'Frontier Airlines'),
    ('CO', 'Continental Airlines'),
    ('AS', 'Alaska Airlines'),
    ('DL', 'Delta Airlines')
)

class SearchForm(forms.Form):
    departure_code = forms.CharField(label='Departure Code', max_length=3)
    arrival_code = forms.CharField(label='Arrival Code', max_length=3)

    airline = forms.ChoiceField(choices=AIRLINES, required=True)
