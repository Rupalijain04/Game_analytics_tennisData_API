import requests
import pandas as pd

api_key = "xS2cb0L43psFWnkyd5i04ADBNPebgUGf4LtuP3wo"

# Call Rankings API
url = f"https://api.sportradar.com/tennis/trial/v3/en/rankings.json?api_key={api_key}"
response = requests.get(url)
data = response.json()
print(data.keys())

# print(len(data['rankings']))
# Understand structure
print(data['rankings'][0])

# Extract Inner Rankings
all_rankings = []

for group in data['rankings']:
    all_rankings.extend(group.get('competitor_rankings', []))

print(len(all_rankings))   # now you should see MANY rows

# Extract Rankings Table
rankings = data['rankings']

ranking_rows = []
for r in all_rankings:
    comp = r.get('competitor')
    
    if comp:
        ranking_rows.append({
            "rank": r.get('rank'),
            "movement": r.get('movement'),
            "points": r.get('points'),
            "competitions_played": r.get('competitions_played'),
            "competitor_id": comp.get('id')   # foreign key
        })
ranking_df = pd.DataFrame(ranking_rows)
print(ranking_df.head())

# Extract Competitors Table
competitor_rows = []
for r in all_rankings:
    comp = r.get('competitor')
    
    competitor_rows.append({
        "competitor_id": comp.get('id') if comp else None,
        "name": comp.get('name') if comp else None,
        "country": comp.get('country') if comp else None,
        "country_code": comp.get('country_code') if comp else None,
        "abbreviation": comp.get('abbreviation') if comp else None
    })
competitor_df = pd.DataFrame(competitor_rows)
print(competitor_df.head())

# Save Both Tables
ranking_df.to_csv(r"C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/Final Project/Rankings/ranking.csv", index=False)

competitor_df.to_csv(r"C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/Final Project/Rankings/competitor.csv", index=False)