import sys
import os
import django

sys.path.append('/django')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airontime.settings")
django.setup()

from flights.models import DisplayFlight, Flight



# Helper Functions
def roundto5(x, base=5):
    return int(base * round(float(x)/base))


# ////////////////////////////////////////////////

objs = []

iden = 1

while(1):
    try:
        current_value = Flight.objects.get(id = iden)
        iden = iden+1
        print('success at try')

        '''
        print('1')
        cur_value = Flight.objects.all().values()
        print('1.5')

        print(cur_value)
        current_value = dict()
        print('hi')
        current_value=cur_value.pop()
        #TODO: IT IS FAILING HERE RIGHT NOW
        print('2')
        '''
    except:
        object_count = Flight.objects.count()
        if object_count == 0:
            break
            print('break')

        print('continue')
        print('the object count is ')
        print(object_count)
        iden = iden +1
        continue

    print('the id is')
    print(iden)

    flight_variable = Flight.objects.filter(fl_num = current_value.fl_num).filter(carrier = current_value.carrier).filter(origin = current_value.origin).filter(dest = current_value.dest)
    flights = flight_variable.values()
    #flights = Flight.objects.filter(fl_num = current_value.fl_num).filter(carrier = current_value.carrier).filter(origin = current_value.origin).filter(dest = current_value.dest).values()

    OTR = 90
    for value in flights:
        deduct = 0

        #if flight is delayed by more than 10 minutes
        if value['arr_delay_new'] >= 10:
            #print('success at this new error')
            delay = roundto5(value['arr_delay_new'], 5)
            deduct = delay/5
            print('flight was delayed and deduct is')
            print(deduct)

        #if flight is cancelled
        elif value['cancelled'] == 1 or value['diverted'] == 1:
            deduct = 5
            print('flight was CANCELLED')


        #if flight is on time
        elif value['arr_delay_new'] ==0:
            deduct = -0.1
            print('flight on time')


        OTR = int(OTR - deduct)



    #normalizing the value of OTR
    if OTR > 99:
        OTR = 99
    elif OTR < 5:
        OTR = 5

    print(' Normalized OTR is')
    print(OTR)

    objs.append( DisplayFlight(
        unique_carrier = current_value.carrier,
        fl_num = current_value.fl_num,
        origin = current_value.origin,
        dest = current_value.dest,
        OTR = OTR,
        scheduled_departure_time = 0000,
        scheduled_arrival_time = 0000
    )
    )
    print('appended to list')

    print('number of UNIQUE flights is ')
    print(len(objs))

    flight_variable.delete()
    print('that flight is deleted')




print('starting to create objects in bulk')
DisplayFlight.objects.bulk_create(objs)
print('objects bulk created')




# ////////////////
