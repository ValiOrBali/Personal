import requests

# Define the API endpoint URL
api_url = "https://api.example.com"

# Define any required parameters or headers
params = {
    "param1": "value1",
    "param2": "value2"
}

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Make a GET request to the API endpoint
response = requests.get(api_url, params=params, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse the response JSON data
    # Process the data as needed
    print(data)
else:
    print("Request failed with status code:", response.status_code)
