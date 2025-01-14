import requests

# Set up the necessary variables
url = "https://localhost/thehive"  # Replace with your TheHive instance URL
api_key = "VTjUoDxcCXqUsjWYy9NOI9ivva+rJFy6"  # Replace with your actual API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    'X-Organisation': 'bob'
}

# Define the endpoint for listing cases
endpoint = "/api/v1/case/~4136968"

# Send a GET request to list cases
response = requests.get(f"{url}{endpoint}", headers=headers, verify=False)

# Check the response
if response.status_code == 200:
    cases = response.json()
    print("Cases retrieved successfully!")
    print("Total cases:", len(cases))
    for case in cases:
        print(f"Case ID: {case['id']}, Title: {case['title']}, Status: {case['status']}")
else:
    print(f"Failed to retrieve cases. Status code: {response.status_code}")
    print("Response:", response.text)