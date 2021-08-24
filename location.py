import sys

from connector import Connector
from schema import LocationSchema


class Location:

    def lookup(self, ip: str) -> dict:
        
        connector = Connector()

        location_response = connector.connect_to_api(ip)
        location_response['_as'] = location_response.pop('as')
        
        location = LocationSchema(**location_response)

        return location.as_dict()

if __name__ == "__main__":
    try:
        ip = sys.argv[1]
        location = Location()
        print(location.lookup(ip))
    except IndexError:
        print("Enter ip-address as argument when running program [ ./location.py <ip-address> ]")
