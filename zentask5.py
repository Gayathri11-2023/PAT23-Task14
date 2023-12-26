'''
import json
with open('data.json', 'r', encoding = 'utf-8') as file :
    data = file.read()
python_object = json.loads(data)
for item in python_object :
    print(item['name'])

for items in python_object:
    print(items['currencies'])
'''
import requests

def get_countries_with_dollar_currency(url):
    
        # Make a GET request to the given URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            countries_data = response.json()

            # Filter countries with dollar as currency
            dollar_countries = [country['name']['common'] for country in countries_data if 'USD' in country.get('currencies', {})]

            # Display the result
            print("Countries with Dollar as Currency:")
            for country in dollar_countries:
                print(country)
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    

# URL for fetching country data
url = "https://restcountries.com/v3.1/all"

# Call the method with the given URL
get_countries_with_dollar_currency(url)




