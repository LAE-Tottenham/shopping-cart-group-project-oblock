import requests
import math

def postvalidate():
    postc = input("Please input Postcode: ").upper()
    while True:
        url = f"https://api.postcodes.io/postcodes/{postc.replace(' ', '%20')}/validate"  
        validate = requests.get(url)
        if validate.json()['result'] == True:
            print("\nPostcode ("+postc+") is valid")
            break
        else:
            print("Postcode is invalid, Try again")
            postc = input("Please input Postcode: ").upper()
    return postc

def latlong(postc):
    url = f"https://api.postcodes.io/postcodes/{postc.replace(' ', '%20')}/"
    ll = requests.get(url)
    lat = ll.json()['result']['latitude']
    long = ll.json()['result']['longitude']
    area = ll.json()['result']['parliamentary_constituency']
    return {'lat' : lat, 'long' : long, 'area' : area}

def distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6371.0

    distance = R * c

    return distance

def delivery(dist):
    fee = dist * 0.6
    return round(fee, 2)

def slot(delivery_price):
    if delivery_price >= 10:
        days = ("Your package will arrive in 3-4 working days")
    else:
        days = ("Your package will arrive in 5-7 working days")
    return days

def runDelivery():
    postc = postvalidate()
    latlongdata = latlong(postc)
    distance_km = distance(51.6042,-0.067574,latlongdata['lat'],latlongdata['long'])
    print("Area: "+latlongdata["area"])
    print(f"Distance between LAET and Postcode: {distance_km:.2f} kilometers")
    delivery_price = delivery(distance_km)
    days = slot(delivery_price)
    print("\nYour delivery price is: £" + str(delivery_price))
    print(days)
    return delivery_price