import requests

# API endpoint
api_url = "https://api.spacexdata.com/v5/launches/latest"

# Sending a GET request
response = requests.get(api_url)

# Handling the response
if response.status_code == 200:
    # Response content as JSON
    data = response.json()
    
    # Extracting relevant information
    if data:
        mission_name = data["name"]
        launch_date_utc = data["date_utc"]
        rocket_id = data["rocket"]
        
        # Retrieving information about the rocket
        rocket_url = f"https://api.spacexdata.com/v5/rockets/{rocket_id}"
        rocket_response = requests.get(rocket_url)
        
        if rocket_response.status_code == 200:
            rocket_data = rocket_response.json()
            rocket_name = rocket_data["name"]
        else:
            rocket_name = "Unknown" 
        
        # Retrieving information about the launch site
        launchpad_name = data["launchpad"]
        
        # Displaying launch information
        print("Latest SpaceX Launch Information:")
        print(f"Mission Name: {mission_name}")
        print(f"Launch Date (UTC): {launch_date_utc}")
        print(f"Rocket Name: {rocket_name}")
        print(f"Launch Site: {launchpad_name}")
    else:
        print("No data found for the latest launch.")
else:
    print(f"Request failed with status code: {response.status_code}")
