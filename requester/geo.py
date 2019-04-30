import requests
import sys
import logging

from math import sin, cos, sqrt, atan2, radians
from tips import all_to_str


def get_toponym(point):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {"geocode": point, "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    return toponym


def get_map_image(coordinates, scale, l):
    map_api_server = "http://static-maps.yandex.ru/1.x/"

    params = {
        'l': l,
        'll': ','.join(all_to_str(coordinates)),
        'spn': ','.join(all_to_str(scale))
    }

    response = requests.get(map_api_server, params=params)
    img_type = '.png'
    if l[:3] == 'sat':
        img_type = '.jpg'
    map_file = 'temp/map{}'.format(img_type)
    try:
        with open('data/' + map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file

def get_spn(point):
    toponym = get_toponym(point)

    lower_corner = toponym['boundedBy']['Envelope']['lowerCorner']
    upper_corner = toponym['boundedBy']['Envelope']['upperCorner']

    lower_corner = [float(i) for i in lower_corner.split()]
    upper_corner = [float(i) for i in upper_corner.split()]

    delta_x = upper_corner[0] - lower_corner[0]
    delta_y = upper_corner[1] - lower_corner[1]

    return delta_x, delta_y


def get_coordinates(point):
    toponym = get_toponym(point)

    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = [float(i) for i in toponym_coodrinates.split(" ")]

    return toponym_longitude, toponym_lattitude


def get_map_response(params):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    if not response:
        print('No map response')
        return None
    return response


def get_distance(p1, p2):

    R = 6373.0

    lon1 = radians(p1[0])
    lat1 = radians(p1[1])
    lon2 = radians(p2[0])
    lat2 = radians(p2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance