import requests

class BreweryInfo:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
    
            response = requests.get(self.url)
            data = response.json()
            return data
      

    def get_breweries_by_state(self, state):
        breweries = []
        for brewery in self.fetch_data():
            if 'state' in brewery and brewery['state'] == state:
                breweries.append(brewery['name'])
        return breweries

# Instantiate the class with the provided URL
url = "https://api.openbrewerydb.org/v1/breweries"
brewery_info = BreweryInfo(url)

# List the names of breweries in Alaska
alaska_breweries = brewery_info.get_breweries_by_state('Alaska')
print("Breweries in Alaska:", alaska_breweries)

# List the names of breweries in Maine
maine_breweries = brewery_info.get_breweries_by_state('Maine')
print("Breweries in Maine:", maine_breweries)

# List the names of breweries in New York
new_york_breweries = brewery_info.get_breweries_by_state('New York')
print("Breweries in New York:", new_york_breweries)
