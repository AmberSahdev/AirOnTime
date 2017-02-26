
def to_full_name(short):
    names = {'AA' : 'American Airlines',
           'UA' : 'United Airlines',
           'AS' : 'Alaska Airlines',
           'DL' : 'Delta Airlines',
           'F9' : 'Frontier Airlines',
           'B6' : 'Jet Blue Airlines',
           'WN' : 'SouthWest Airlines',
           'NK' : 'Spirit Airlines',
           'VX' : 'Virgin Atlantic'
           }
    return names[short]

def get_url(short):
    names = {'AA' : 'https://www.aa.com',
           'UA' : 'https://www.united.com',
           'AS' : 'https://www.alaskaair.com',
           'DL' : 'https://www.delta.com',
           'F9' : 'https://www.flyfrontier.com',
           'B6' : 'https://www.jetblue.com',
           'WN' : 'https://www.southwest.com',
           'NK' : 'https://www.spirit.com',
           'VX' : 'https://www.virginatlantic.com'
           }
    return names[short]
