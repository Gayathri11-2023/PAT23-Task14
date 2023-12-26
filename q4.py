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

    def count_breweries_with_websites_by_state(self, states):
        breweries_with_websites = {}
        for brewery in self.fetch_data():
            if 'state' in brewery and brewery['state'] in states and 'website_url' in brewery:
                state = brewery['state']
                website_url = brewery['website_url']
                if state not in breweries_with_websites:
                    breweries_with_websites[state] = []
                breweries_with_websites[state].append({"name": brewery['name'], "website": website_url})
        return breweries_with_websites

# Instantiate the class with the provided URL
url = "https://api.openbrewerydb.org/v1/breweries"
brewery_info = BreweryInfo(url)

# Specify the states of interest
target_states = ['Alaska', 'Maine', 'New York']

# Get the count and list of breweries with websites in the specified states
breweries_with_websites_by_state = brewery_info.count_breweries_with_websites_by_state(target_states)

# Display the count and list of breweries with websites in each specified state
for state, breweries_with_websites in breweries_with_websites_by_state.items():
    print(f"{state}: {len(breweries_with_websites)} breweries with websites")
    for brewery in breweries_with_websites:
        print(f"  {brewery['name']}: {brewery['website']}")
