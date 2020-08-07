from math import sin, cos, sqrt, atan2, radians

def GPStoKM(lat1, lon1, lat2, lon2):
    R = 6373.0 # Radius of earth in kilometers 

    # Find the distance delta 
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    print(f"Distance is {round(R * c, 2)} km.")

lat1 = radians(float(input("Enter first latitude: ")))
lon1 = radians(float(input("Enter first longitude: ")))
lat2 = radians(float(input("Enter second latitude: ")))
lon2 = radians(float(input("Enter second longitude: ")))


# Test coordinates
# lat1 = radians(52.2296756)
# lon1 = radians(21.0122287)
# lat2 = radians(52.406374)
# lon2 = radians(16.9251681)

GPStoKM(lat1, lon1, lat2, lon2)
