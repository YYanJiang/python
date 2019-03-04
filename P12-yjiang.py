import urllib.request, urllib.parse, urllib.error
import json
from math import radians, cos, sin, asin, sqrt ,fabs
  
# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

#while True:
   
def getlocation(): 
#while True:    
    address = input('Enter location: ')
    if len(address) < 1: 
        return 0

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    #print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        #print(data)
        #continue

    #print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    
    print(location)
    return lat,lng
    

def get_distance_hav(lat0, lng0, lat1, lng1):
    EARTH_RADIUS=3959
 
    lat0 = radians(lat0)  
    lat1 = radians(lat1)  
    lng0 = radians(lng0)  
    lng1 = radians(lng1)  
   
    dlng = fabs(lng0 - lng1)  
    dlat = fabs(lat0 - lat1)  
    #h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)  
    h=sin(dlat/2)**2 + cos(lat0) * cos(lat1) * sin(dlng/2)**2
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))  
   
    return distance  


#lon1,lat1 =(40.7439905,-74.0323626)   hoboken 

lon1,lat1 = getlocation()
lon2,lat2 = getlocation()
d2 = get_distance_hav(lon1,lat1,lon2,lat2)
print('\nThe The distance is about',round(d2,1),'miles.')
