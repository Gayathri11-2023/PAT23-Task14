
import requests

def get_countries_with_euro_currency(url):
    
        
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            
            countries_data = response.json()

            # Filter countries with Euro as currency
            euro_countries = [country['name']['common'] for country in countries_data if 'EUR' in country.get('currencies', {})]

            # Display the result
            print("Countries with Euro as Currency:")
            for country in euro_countries:
                print(country)
        else:
            print(f"Error: Status code: {response.status_code}")
    

url = "https://restcountries.com/v3.1/all"

# Call the method with the given URL
get_countries_with_euro_currency(url)
