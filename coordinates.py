# Import the necessary library
import requests

# store google api key in txt and read the file
def get_map_api_key():
    with open('api_key/google_api_key.txt','r') as file:
        return file.read().strip()
# store the google api key in a variable
google_api_key=get_map_api_key()

def get_coordinates(location):

# store URL of Google Geocoding API by passing location and api key
    URL = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}+UK&key={google_api_key}'
# store response
    resp = requests.get(URL)

# error handling
    if resp.status_code !=200:
        print(f"Error fetching Geo data for {location}: {resp.status_code}")

# store response in json format
    results = resp.json()["results"]
# store and print address to check correct location is returned
#    address = results[0]["formatted_address"]
#    print(f"The address for {location} is:\n", address)

# Store Geo params including lat and lon
    geo = results[0]["geometry"]
    lat = geo['location']['lat']
    lon = geo['location']['lng']
# print lat and lon to check the output is correct
#    print("The latitude is: ", lat)
#    print("The longitude is: ", lon)

# return coordinates from this function to be used in main.py
    coord = [lat, lon]
    return coord