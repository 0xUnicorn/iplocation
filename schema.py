from dataclasses import dataclass
import json


@dataclass
class LocationSchema:

    status: str
    country: str
    countryCode: str
    region: str
    regionName: str
    city: str
    zip: str
    lat: float
    lon: float
    timezone: str
    isp: str
    org: str
    query: str
    _as: str

    def as_dict(self):
        return json.dumps(
            {
                "status": self.status,
                "country": self.country,
                "countryCode": self.countryCode,
                "region": self.region,
                "regionName": self.regionName,
                "city": self.city,
                "zip": self.zip,
                "lat": self.lat,
                "lon": self.lon,
                "timezone": self.timezone,
                "isp": self.isp,
                "org": self.org,
                "as": self._as,
                "query": self.query
            },
            indent=4
        )
