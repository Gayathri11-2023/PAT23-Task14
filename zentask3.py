import requests
class get_data():
      
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
            response = requests.get(self.url)
            data = response.json()
            return data
 # create a method to fetch all json data from the data.Json
    def fetch_all_data():
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
    # Check if the request was successful (status code 200)
        if response.status_code == 200 :
          data = response.json()
          return data
        else:
             print("f Error: Unable to fetch data. Status code: {response.status_code}")
             return None
all_data = get_data.fetch_all_data()

# Check if data is fetched successfully
if all_data:
    # Now you can work with the 'all_data' variable, which contains the JSON data.
    print(all_data)


