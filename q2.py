import requests

class BreweryInfo:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        
            response = requests.get(self.url)
            data = response.json()
            return data
        

    def count_breweries_by_state(self, states):
        
        state_counts = {}
        for brewery in self.fetch_data():
            if 'state' in brewery and brewery['state'] in states:
                state = brewery['state']
                state_counts[state] = state_counts.get(state, 0) + 1
        return state_counts

# Instantiate the class with the provided URL
url = "https://api.openbrewerydb.org/v1/breweries"
brewery_info = BreweryInfo(url)

# Specify the states of interest
target_states = ['Alaska', 'Maine', 'New York']

# Get the count of breweries in the specified states
breweries_by_state = brewery_info.count_breweries_by_state(target_states)

# Display the count of breweries in each specified state
for state, count in breweries_by_state.items():
    print(f"{state}: {count} breweries")
