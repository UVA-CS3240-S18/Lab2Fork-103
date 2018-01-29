# Mark Sherriff (mss2x)

import math
import webbrowser

google_maps_url = "https://www.google.com/maps/@35.372742,-81.954957,15z?hl=en"

def distance_between(lat_1, lon_1, lat_2, lon_2):
    theta = lon_1 - lon_2
    dist = sin_conversion(lat_1) * sin_conversion(lat_2) + cos_conversion(lat_1) * cos_conversion(lat_2) * cos_conversion(theta)
    dist = math.acos(dist)
    dist = dist * 180.0 / math.pi
    dist = dist * 60 * 1.1515

    return dist

def sin_conversion(number):
    conversion = math.sin(number * math.pi / 180.0)
    return conversion

def cos_conversion(number):
    conversion = math.cos(number * math.pi / 180.0)
    return conversion

#lat = float(input("Current latitude: "))
#lon = float(input("Current longitude: "))

lat = 38.0322727
lon = -78.50997339999999
datafile = open("wendys.csv", "r")

closest_dist = 200
closest_wendys = ""

for line in datafile:
    entry = line.split(";")
    dist_to_wendys = distance_between(lat, lon, float(entry[0]), float(entry[1]))
    if dist_to_wendys < closest_dist:
        google_maps_url = "https://www.google.com/maps?q=" + str(entry[4]) + "+" + str(entry[5]) + "+" + str(entry[6])
        print(google_maps_url)
        closest_dist = dist_to_wendys
        closest_wendys = entry[2]

datafile.close()

print("The closest Wendy's (", closest_wendys, ") is", closest_dist, "miles away.")
google_maps_url = google_maps_url.replace(' ', '+')
webbrowser.open(google_maps_url)

