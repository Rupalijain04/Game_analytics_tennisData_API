import requests
import pandas as pd

api_key = "xS2cb0L43psFWnkyd5i04ADBNPebgUGf4LtuP3wo"

# Call Complexes API
url = f"https://api.sportradar.com/tennis/trial/v3/en/complexes.json?api_key={api_key}"
response = requests.get(url)
print("Status Code:", response.status_code)
data = response.json()
print(data.keys())

# Understand structure
print(data['complexes'][0])

# Extract Complexes table
complexes = data['complexes']
complex_rows = []
for comp in complexes:
    complex_rows.append({
        "complex_id": comp['id'],
        "complex_name": comp['name']
    })
complex_df = pd.DataFrame(complex_rows)
print(complex_df.head())

# Extract Venues table
venue_rows = []
for comp in complexes:
    for venue in comp.get('venues',[]):
        venue_rows.append({
            "venue_id": venue['id'],
            "venue_name": venue['name'],
            "city": venue.get('city_name'),
            "country": venue.get('country_name'),
            "country_code": venue.get('country_code'),
            "timezone": venue.get('timezone'),
            "complex_id": comp['id']   
       })
venue_df = pd.DataFrame(venue_rows)
print(venue_df.head())

# Save Both Tables
complex_df.to_csv(r"C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/Final Project/Complexes/complexes.csv", index=False)

venue_df.to_csv(r"C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/Final Project/Complexes/venues.csv", index=False)