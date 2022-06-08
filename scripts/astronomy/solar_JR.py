#!/usr/bin/env python3
import datetime
import os
import requests
import sys

ASTRONOMYAPI_ID = os.environ.get("ASTRONOMYAPI_ID")
ASTRONOMYAPI_SECRET = os.environ.get("ASTRONOMYAPI_SECRET")

def get_observer_location():
    """Returns the longitude and latitude for the location of this machine.
    Returns:
    str: latitude
    str: longitude"""
    url = "https://ip-api.com/json/"
    try:
        response = requests.get(url)
        if not response.status_code == 200:
            return None, None
    except requests.exceptions.ConnectionError:
        return None, None
    except requests.exceptions.Timeout:
        return None, None
    data = response.json()
    # NOTE: Replace with your real return values!
    return data.get("lat"), data.get("long")

def get_sun_position(latitude, longitude, body="sun"):
    """Returns the current position of the sun in the sky at the specified location
    Parameters:
    latitude (str)
    longitude (str)
    Returns:
    float: azimuth
    float: altitude
    """
    body = body or "sun"
    url = f"https://api.astronomyapi.com/api/v2/bodies/positions/{body}"
    now = datetime.datetime.now()
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": 0,
        "from_date": now.date().isoformat(),
        "to_date": now.date().isoformat(),
        "time": now.strftime("%H:%M:%S"),
    }
    try:
        response = requests.get(
            url, params=params,
            auth=(ASTRONOMYAPI_ID, ASTRONOMYAPI_SECRET))
        if not response.status_code == 200:
            return None, None
    except requests.exceptions.ConnectionError:
        return None, None
    except requests.exceptions.Timeout:
        return None, None
    data = response.json()
    position = data["position"]["horizontal"]
    alt = position["altitude"]["degrees"]
    az = position["azimuth"]["degrees"]
    return az, alt

def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates
    Parameters:
    azimuth (float)
    altitude (float)"""
    print(
        f"The Sun is currently at: " "{altitude} deg altitude, {azimuth} deg azimuth."
    )

if __name__ == "__main__":
    latitude, longitude = get_observer_location()
    if latitude is None or longitude is None:
        print("Could not find your location by IP!")
        sys.exit(1)
    azimuth, altitude = get_sun_position(latitude, longitude)
    if azimuth is None or altitude is None:
        print("Could not get Sun position from Astronomy API")
        sys.exit(2)
    print_position(azimuth, altitude)

And here are some sample unit tests (with mocking):
test_solar.py

"""Unit tests for solar.py Astronomy API client"""
from requests import exceptions
from unittest.mock import patch
import solar

def test_get_observer_location_success():
    """Test correct values are returned during a successful API call"""
    with patch('requests.get') as mock_get:
        expected = {
            "lat": 32.765,
            "long": 45.123,
        }
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected
        lat, lon = solar.get_observer_location()
        mock_get.assert_called_with("https://ip-api.com/json/")
        assert lat == expected["lat"]
        assert lon == expected["long"]

def test_get_observer_location_server_error():
    """Test error value is returned for a HTTP Server Error (500)"""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        lat, lon = solar.get_observer_location()
        mock_get.assert_called_with("https://ip-api.com/json/")
        assert lat is None
        assert lon is None

def test_get_observer_location_connectionerror():
    """Test error value is returned for a ConnectionError exception"""
    with patch('requests.get') as mock_get:
        # Causes Mock requests.get to raise an exception
        # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
        mock_get.side_effect = exceptions.ConnectionError
        lat, lon = solar.get_observer_location()
        mock_get.assert_called_with("https://ip-api.com/json/")
        assert lat is None
        assert lon is None

def test_get_observer_location_timeouterror():
    """Test error value is returned for a Timeout exception"""
    with patch('requests.get') as mock_get:
        # Causes Mock requests.get to raise an exception
        # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
        mock_get.side_effect = exceptions.Timeout
        lat, lon = solar.get_observer_location()
        mock_get.assert_called_with("https://ip-api.com/json/")
        assert lat is None
        assert lon is None

def test_get_sun_position_success():
    """Test correct values are returned during a successful API call"""
    with patch('requests.get') as mock_get:
        # Mimic the structure of the response, but only worry about the pieces
        # we actually access in our function under test.
        expected = {
            "position": {
                "horizontal": {
                    "altitude": {
                        "degrees": 45.123,
                    },
                    "azimuth": {
                        "degrees": 32.125,
                    },
                },
            },
        }
        expected_az = expected["position"]["horizontal"]["azimuth"]["degrees"]
        expected_alt = expected["position"]["horizontal"]["altitude"]["degrees"]
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected
        az, alt = solar.get_sun_position(123, 456)
        assert az == expected_az
        assert alt == expected_alt

def test_get_sun_position_server_error():
    """Test error value is returned for a HTTP Server Error (500)"""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        az, alt = solar.get_sun_position(123, 456)
        assert az is None
        assert alt is None

def test_get_sun_position_connectionerror():
    """Test error value is returned for a ConnectionError exception"""
    with patch('requests.get') as mock_get:
        # Causes Mock requests.get to raise an exception
        # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
        mock_get.side_effect = exceptions.ConnectionError
        az, alt = solar.get_sun_position(123, 456)
        assert az is None
        assert alt is None

def test_get_sun_position_timeout():
    """Test error value is returned for a Timeout exception"""
    with patch('requests.get') as mock_get:
        # Causes Mock requests.get to raise an exception
        # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
        mock_get.side_effect = exceptions.Timeout
        az, alt = solar.get_sun_position(123, 456)
        assert az is None
        assert alt is None

