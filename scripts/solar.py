#!/usr/bin/env python3
# Test Change
import requests
import json
import argparse
from datetime import datetime
import pytz
from pprint import pprint
from requests.auth import HTTPBasicAuth

ASTRONOMYAPI_ID = "c24f965e-d754-4e7f-ad38-06c793c2d279"
ASTRONOMYAPI_SECRET = "b586c68a0970564b265d639a9c730e1f1e8c7ac5e098e76d79c3e9f6807ce68804bf55e9f765943365a28b2766decc9b25cb7783f8ff3e984108e74528e04b91a6a88c8ec91055661d17d04c40de5213a98f773d3b8c586d5a78b10b9a517861d60985dcbcb20f767b614fab98d15301"


def get_observer_location():
    """Returns the longitude and latitude for the location of this machine.
    Returns:
    str: latitude
    str: longitude"""

    ob_location = requests.get(
        "http://ip-api.com/json/?fields=lat,lon,region,city,query"
    )
    ob_data = ob_location.json()
    latitude = ob_data.get("lat")
    longitude = ob_data.get("lon")
    state = ob_data.get("region")
    city = ob_data.get("city")
    #   print(ob_location.text)
    return latitude, longitude, state, city


def get_sun_position(latitude, longitude):
    """Returns the current position of the sun in the sky at the specified location
    Parameters:
    latitude (str)
    longitude (str)
    Returns:
    float: azimuth
    float: altitude"""

    current_time = datetime.now(pytz.timezone("US/Eastern"))
    fmt = "%H:%M:%S"
    time = current_time.strftime(fmt)
    query = {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": 0,
        "from_date": datetime.today().strftime("%Y-%m-%d"),
        "to_date": datetime.today().strftime("%Y-%m-%d"),
        "time": time,
    }
    sun_location = requests.get(
        f"https://api.astronomyapi.com/api/v2/bodies/positions/{celestial}",
        auth=HTTPBasicAuth(ASTRONOMYAPI_ID, ASTRONOMYAPI_SECRET),
        params=query,
    )
    sun_data = sun_location.json()["data"]["table"]["rows"][0]["cells"][0]
    azimuth = sun_data["position"]["horizonal"]["azimuth"]["degrees"]
    azimuth_str = sun_data["position"]["horizonal"]["azimuth"]["string"]
    altitude = sun_data["position"]["horizonal"]["altitude"]["degrees"]
    altitude_str = sun_data["position"]["horizonal"]["altitude"]["string"]
    distance = sun_data["distance"]["fromEarth"]["km"]
    magnitude = sun_data["extraInfo"]["magnitude"]
    #   print(sun_location.text)
    return (
        current_time,
        float(azimuth),
        str(azimuth_str),
        float(altitude),
        str(altitude_str),
        round(float(distance)),
        float(magnitude),
    )


def print_position(
    current_time, azimuth, azimuth_str, altitude, altitude_str, distance, magnitude
):
    """Prints the position of the sun in the sky using the supplied coordinates
    Parameters:
    azimuth (float)
    altitude (float)"""

    now = datetime.now()
    #   print("From your location in", city, ",", state, "the Sun is currently at: Azimuth=", azimuth, ", Altitude=", altitude)

    print(
        "\n",
        "From",
        city,
        ",",
        state,
        "at",
        current_time.strftime("%I:%M %p"),
        "on",
        now.strftime("%B %d, %Y"),
        ":",
        "\n\n",
        celestial,
        ":",
        "\n",
        "\t",
        "Distance from Earth:",
        format(distance, ","),
        "km",
        "\n",
        "\t",
        "Magnitude:",
        magnitude,
        "\n",
        "\t",
        "Position:",
        "\n",
        "\t",
        "Azimuth:",
        azimuth_str,
        "\n",
        "\t",
        "Altitude:",
        altitude_str,
        "\n",
    )


if __name__ == "__main__":
    try:
        celestial = "Sun"
        latitude, longitude, state, city = get_observer_location()
        ip_latitude, ip_longitude = latitude, longitude
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument("--at")
        parser.add_argument("--from_pos")
        parser.add_argument("celestial", nargs="?")
        args = parser.parse_args()
        if args.at:
            time_date = args.at.split("T")
            time = time_date[1]
            current_date = time_date[0]
        if args.from_pos:
            position = args.from_pos.split(",")
            latitude = position[0].split("=")[1]
            longitude = position[1].split("=")[1]
        if args.celestial:
            celestial = args.celestial.capitalize()
        (
            current_time,
            azimuth,
            azimuth_str,
            altitude,
            altitude_str,
            distance,
            magnitude,
        ) = get_sun_position(latitude, longitude)
        print_position(
            current_time,
            azimuth,
            azimuth_str,
            altitude,
            altitude_str,
            distance,
            magnitude,
        )

    # if __name__ == "__main__":
    #     try:
    #         now = datetime.now()
    #         current_date = now.strftime("%G-%m-%d")
    #         time = now.strftime("%X")
    #         # celestial = 'Sun'
    #         latitude, longitude, state, city = get_observer_location()
    #         ip_latitude, ip_longitude = latitude, longitude
    #         parser = argparse.ArgumentParser(add_help=True)
    #         parser.add_argument('--at')
    #         parser.add_argument('--from_pos')
    #         parser.add_argument('celestial', nargs='?')
    #         args = parser.parse_args()
    #         if args.at:
    #            time_date = args.at.split('T')
    #            time = time_date[1]
    #            current_date = time_date[0]
    #         if args.from_pos:
    #            position = args.from_pos.split(',')
    #            latitude = position[0].split('=')[1]
    #            longitude = position[1].split('=')[1]
    #         if args.celestial:
    #            celestial = args.celestial.capitalize()
    #         current_time, azimuth, azimuth_str, altitude, altitude_str, distance, magnitude = get_sun_position(latitude, longitude)
    #         print_position(current_time, azimuth, azimuth_str, altitude, altitude_str, distance, magnitude)
    except IndexError:
        print("There was an index error")
    except NameError:
        print("A name is not defined, please check your code")
    except AttributeError:
        print("There is an issue with an attribute, please check your code")
    # except KeyError:
    #     print('Please check your command line arguments for errors and try again')
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
