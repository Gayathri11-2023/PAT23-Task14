import requests

class BreweryInfo:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def count_brewery_types_by_state(self, states):
        brewery_types_count = {}
        for brewery in self.fetch_data():
            if 'state' in brewery and brewery['state'] in states and 'brewery_type' in brewery:
                state = brewery['state']
                brewery_type = brewery['brewery_type']
                state_brewery_types = brewery_types_count.setdefault(state, {})
                state_brewery_types[brewery_type] = state_brewery_types.get(brewery_type, 0) + 1
        return brewery_types_count

# Instantiate the class with the provided URL
url = "https://api.openbrewerydb.org/v1/breweries"
brewery_info = BreweryInfo(url)

# Specify the states of interest
target_states = ['Alaska', 'Maine', 'New York']

# Get the count of brewery types in the specified states
brewery_types_by_state = brewery_info.count_brewery_types_by_state(target_states)

# Display the count of brewery types in each specified state
for state, types_count in brewery_types_by_state.items():
    print(f"{state}:")
    for brewery_type, count in types_count.items():
        print(f"  {brewery_type}: {count} breweries")
