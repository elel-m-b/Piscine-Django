#!/usr/bin/env python3
"""
Exercise 00: Antigravity
Compute and display a typical geohash from a latitude and a longitude.

Authorized modules: sys, antigravity
"""
import sys

__BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"


def _to_float(value, name):
    """Try to convert a parameter to a float, raise ValueError otherwise."""
    try:
        return float(value)
    except ValueError:
        raise ValueError("'{}' is not a valid number for {}".format(value, name))


def encode_geohash(latitude, longitude, precision=12):
    """
    Encode a (latitude, longitude) pair into a geohash string.

    latitude  : float in [-90, 90]
    longitude : float in [-180, 180]
    precision : number of characters of the resulting geohash (default 12)
    """
    if not (-90.0 <= latitude <= 90.0):
        raise ValueError("latitude must be between -90 and 90")
    if not (-180.0 <= longitude <= 180.0):
        raise ValueError("longitude must be between -180 and 180")
    if precision < 1:
        raise ValueError("precision must be a positive integer")

    lat_interval = (-90.0, 90.0)
    lon_interval = (-180.0, 180.0)

    geohash = []
    bits = [16, 8, 4, 2, 1]
    bit = 0
    ch = 0
    even = True

    while len(geohash) < precision:
        if even:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if longitude > mid:
                ch |= bits[bit]
                lon_interval = (mid, lon_interval[1])
            else:
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if latitude > mid:
                ch |= bits[bit]
                lat_interval = (mid, lat_interval[1])
            else:
                lat_interval = (lat_interval[0], mid)

        even = not even

        if bit < 4:
            bit += 1
        else:
            geohash.append(__BASE32[ch])
            bit = 0
            ch = 0

    return "".join(geohash)


def geohashing(argv):
    """
    Parse command line parameters and print the resulting geohash.

    Expected usage:
        python3 geohashing.py <latitude> <longitude> [precision]
    """
    try:
        if len(argv) < 3:
            raise ValueError(
                "usage: python3 geohashing.py <latitude> <longitude> [precision]"
            )

        latitude = _to_float(argv[1], "latitude")
        longitude = _to_float(argv[2], "longitude")

        precision = 12
        if len(argv) >= 4:
            try:
                precision = int(argv[3])
            except ValueError:
                raise ValueError("precision must be an integer")

        result = encode_geohash(latitude, longitude, precision)
        print(result)

    except ValueError as error:
        print("Error: {}".format(error))
    except Exception as error:
        print("Error: an unexpected error occurred ({})".format(error))


if __name__ == '__main__':
    geohashing(sys.argv)
