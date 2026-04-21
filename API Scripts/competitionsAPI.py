import requests
import pandas as pd

api_key = "xS2cb0L43psFWnkyd5i04ADBNPebgUGf4LtuP3wo"

# Call Competitions API
url = f"https://api.sportradar.com/tennis/trial/v3/en/competitions.json?api_key={api_key}"

response = requests.get(url)
print("Status Code:", response.status_code)
data = response.json()
print(data.keys())

# Understand structure
print(data['competitions'][0])

# Extract Competitions table
competitions = data['competitions']
comp_rows = []
for comp in competitions:
    comp_rows.append({
        "competition_id": comp['id'],
        "competition_name": comp['name'],
        "type": comp.get('type'),
        "gender": comp.get('gender'),
        "category_id": comp['category']['id'],
        "category_name": comp['category']['name']
    })
comp_df = pd.DataFrame(comp_rows)
print(comp_df.head())

# Extract Categories table
category_rows = []
for comp in competitions:
    category_rows.append({
        "category_id": comp['category']['id'],
        "category_name": comp['category']['name']
    })
category_df = pd.DataFrame(category_rows).drop_duplicates()

print(category_df.head())

# Save Both tables
comp_df.to_csv(r"C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/Final Project/Competitions/competitions.csv", index=False)

category_df.to_csv(r"C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/Final Project/Competitions/categories.csv", index=False)


