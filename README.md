# IP-LOCATION

## Description

This package uses `https://ip-api.com` for performing ip-based location lookups \
Developed for use in a BornHack 2021 application. \

The reason for developing this is for not exceding the limit of 45 request/min on the API.

## Usage

> from iplocation import Location \
> location = Location() \
> location_response = location.lookup(IP-ADDRESS)

### Response

```json
{
    "status": "success",
    "country": "United States",
    "countryCode": "US",
    "region": "MO",
    "regionName": "Missouri",
    "city": "El Dorado Springs",
    "zip": "64744",
    "lat": 38.0306,
    "lon": -94.0897,
    "timezone": "America/Chicago",
    "isp": "BornHack IVS",
    "org": "BornHack IVS",
    "as": "AS208647 BornHack IVS",
    "query": "151.216.8.52"
}
```