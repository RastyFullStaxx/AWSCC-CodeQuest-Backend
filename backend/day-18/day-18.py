import requests
import json

# API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"

# Set Custom Headers
headers = {'User-Agent': 'MyApp/1.0'}

# Construct a GET request with custom headers
response_get = requests.get(url, headers=headers)

# Send the GET Request
print("GET Request:")
print("Status Code:", response_get.status_code)
print("Response Headers:", response_get.headers)
print("Response Content:", response_get.text)
print()

# Prepare Data for POST Request
new_post_data = {
    'title': 'Dictionary',
    'body': 'This is my entry for day 18'
}

# Send a POST Request
response_post = requests.post(url, headers=headers, json=new_post_data)

# Inspect the POST Response
print("POST Request:")
print("Status Code:", response_post.status_code)
print("Response Content:", response_post.text)
