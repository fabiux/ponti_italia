"""
Module: wwl
Compute distance and azimuth between two Maidenhead squares.

@author: Fabio Pani (IZ2UQF)
@version: 0.2_beta
"""
from math import radians, degrees, pi, sin, cos, atan2, sqrt, pow

WWL_LEN = 6
EARTHRADIUS = 6371.33

bearing = 0
distance = 0


def is_valid_locator(wwl):
    if len(wwl) != WWL_LEN:
        return False
    return not(wwl[0] < 'A' or wwl[0] > 'R' or wwl[1] < 'A' or wwl[1] > 'R' or wwl[2] < '0' or
               wwl[2] > '9' or wwl[3] < '0' or wwl[3] > '9' or wwl[4] < 'A' or wwl[4] > 'X' or
               wwl[5] < 'A' or wwl[5] > 'X')


def convert_locator(wwl):
    loc = dict()
    charbase = ord('A')
    numbase = ord('0')
    loc['latitude'] = radians((ord(wwl[1]) - charbase) * 10.0 - 90.0 + (ord(wwl[3]) - numbase) +
                              (ord(wwl[5]) - charbase) / 24.0 + (1.0 / 48.0))
    loc['longitude'] = radians((ord(wwl[0]) - charbase) * 20.0 - 180.0 + (ord(wwl[2]) - numbase) * 2.0 +
                               (ord(wwl[4]) - charbase) / 12.0 + (1.0 / 24.0))
    return loc


def bearing_distance(my_location, dx_location):
    global bearing
    global distance

    hn = my_location['latitude']
    he = my_location['longitude']
    n = dx_location['latitude']
    e = dx_location['longitude']

    co = cos(he - e) * cos(hn) * cos(n) + sin(hn) * sin(n)
    ca = atan2(sqrt(1 - pow(co, 2)), co)
    az = atan2(sin(e - he) * cos(n) * cos(hn), sin(n) - sin(hn) * cos(ca))
    if az < 0:
        az += 2.0 * pi

    bearing = degrees(az)
    distance = EARTHRADIUS * ca
    return


def get_longitude(location):
        return round(degrees(location['longitude']), 4)


def get_latitude(location):
    return round(degrees(location['latitude']), 4)
