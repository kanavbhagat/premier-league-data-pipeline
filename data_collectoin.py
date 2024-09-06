import requests
import json

def get_premier_league_data():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all"
    
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "d8071ff1e9msh82a7aa69a040cadp1c813ajsnc801c02fd27d"
    }
    
    response = requests.get(url, headers=headers, verify = False)
    return response.json()

if __name__ == "__main__":
    data = get_premier_league_data()
    with open('premier_league_data.json', 'w') as f:
        json.dump(data, f)
