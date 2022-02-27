import pandas as pd
import math

def pushandpull(lat, lng, score, contact):
    centre_locations = pd.read_csv("total_database1.csv")
    min_dist = []
    for i in range(len(centre_locations.index)):
        x1 = centre_locations["latitudes"][i]
        y1 = centre_locations["longitudes"][i]
        minboi = math.sqrt((lat-x1)*(lat-x1) + (lng-y1)*(lng-y1))
        min_dist.append(minboi)

    centre_locations['minimum distance'] = min_dist
    #print(centre_locations)


    centre_locations.sort_values(by=['minimum distance'], inplace=True)

    if score > 7:
        statement = "It is urgent that you get professional help. You are being directed to hospitals and doctors near you."
        admit_locations = centre_locations.loc[centre_locations['Doctor Consultation AND ADMIT'] == 'Y']
        admits_list = admit_locations.values.tolist()
        final_list=admits_list

    elif 7 >= score >= 6:
        statement = "Must do a professional covid-19 test.You may be infected with covid-19. We will be accessing your devices information to help you find the nearest open covid testing center. "
        testing_locations = centre_locations.loc[centre_locations['testing'] == 'Y']
        testing_list = testing_locations.values.tolist()
        final_list=testing_list

    elif 5 >= score >= 4:
        statement = "You might be infected with covid-19. You need to do a take-at-home test.  We will be accessing your devices information to help you find the nearest store which will sell take-at-home covid tests"
        home_locations = centre_locations.loc[centre_locations['home testing'] == 'Y']
        home_list = home_locations.values.tolist()
        final_list=home_list

    elif 0 < score <= 3:
        statement = "you must isolate yourself for 5 days, if no more symptoms then you are not infected. We will be accessing your devices information and providing you with information regarding where resources such as masks are available. "
        mask_locations = centre_locations.loc[centre_locations['Masks'] == 'Y']
        mask_list = mask_locations.values.tolist()
        final_list = mask_list
    
    else:
        statement = "Isolate for 7 days if no more symptoms then you are not infected"
        final_list = 'None'

    if contact == 1:
        statement = "You must Isolate for 14 days and do a covid-19 test.We will be accessing your devices information to help you find the nearest open covid testing center"

    return [statement, final_list, min_dist]



lat=-16.63007
lng=-71.06416            
score=8
contact=1

new__1 = pushandpull(lat, lng, score, contact)

for i in new__1:
    print(i)