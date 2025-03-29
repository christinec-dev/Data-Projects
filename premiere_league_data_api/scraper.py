# Imports
import requests
import pandas as pd
import os
import time
from dotenv import load_dotenv


#region EXTRACTION

# Load environment variables from .env file
load_dotenv()

# API endpoints
COMPETITION_ID = 'PL'
BASE_URL_STANDINGS = f'http://api.football-data.org/v4/competitions/{COMPETITION_ID}/standings'
BASE_URL_TEAMS = 'http://api.football-data.org/v4/teams/{id}'
BASE_URL_SCORERS = f'http://api.football-data.org/v4/competitions/{COMPETITION_ID}/scorers'

# Headers
REQUEST_HEADER = {
    'X-Auth-Token': os.getenv("API_KEY"),
    'User-Agent': os.getenv("USER_AGENT"),
    'Accept-Language': 'en-US, en;q=0.5'
}

# Function to get standings
def get_standings(season=None):
    params = {'season': season}
    response = requests.get(url=BASE_URL_STANDINGS, headers=REQUEST_HEADER, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limit exceeded. Waiting before retrying...")
        time.sleep(60)  # Wait for 60 seconds before retrying
        return get_standings(season)
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to get team details
def get_team(team_id):
    response = requests.get(url=BASE_URL_TEAMS.format(id=team_id), headers=REQUEST_HEADER)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limit exceeded. Waiting before retrying...")
        time.sleep(60)
        return get_team(team_id)
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to get top scorers
def get_top_scorers(season=None):
    params = {'season': season}
    response = requests.get(url=BASE_URL_SCORERS, headers=REQUEST_HEADER, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limit exceeded. Waiting before retrying...")
        time.sleep(60)
        return get_top_scorers(season)
    else:
        print(f"Error: {response.status_code}")
        return None

# Fetch data
standings_data = get_standings(season=2024)
scorers_data = get_top_scorers(season=2024)

# Combine data
if standings_data and scorers_data:
    standings_df = pd.DataFrame(standings_data['standings'][0]['table'])
    scorers_df = pd.DataFrame(scorers_data['scorers'])

    # Add coach, top scorer, goals, and penalties to standings
    standings_df['coach'] = None
    standings_df['top_scorer'] = None
    standings_df['goals'] = 0
    standings_df['penalties'] = 0

    for index, row in standings_df.iterrows():
        team_id = row['team']['id']
        
        # Get team details
        team_data = get_team(team_id)
        if team_data:
            coach_name = team_data.get('coach', {}).get('name', 'Unknown')
            standings_df.at[index, 'coach'] = coach_name
        
        # Get top scorer for the team
        team_scorers = scorers_df[scorers_df['team'].apply(lambda x: x.get('id') == team_id if isinstance(x, dict) else False)]
        if not team_scorers.empty:
            top_scorer_name = team_scorers.iloc[0]['player']['name']
            goals = team_scorers.iloc[0]['goals']
            assists = team_scorers.iloc[0]['assists']
            penalties = team_scorers.iloc[0].get('penalties', 0)
            standings_df.at[index, 'top_scorer'] = top_scorer_name
            standings_df.at[index, 'goals'] = goals
            standings_df.at[index, 'assists'] = assists
            standings_df.at[index, 'penalties'] = penalties
else:
    print("Failed to retrieve data.")

# Extract only the name from team column
df = standings_df
df['team'] = df['team'].apply(lambda x: x['name'] if isinstance(x, dict) else None) 
df.head()

#endregion

#region PREPROCESSING

# Replace missing values
df_copy = df.copy()
df_copy['top_scorer'] = df_copy['top_scorer'].fillna("Unknown")
df_copy['penalties'] = df_copy['penalties'].fillna(0)
df_copy['assists'] = df_copy['assists'].fillna(0)
print("\nMissing values: ")
print(df_copy.isna().sum())

# Rename columns
df_copy.columns = df_copy.columns.str.capitalize()
df_copy.rename({"Playedgames": "Played Games", "Goalsfor": "Goals For", "Goalsagainst": "Goals Against", "Goaldifference": "Goal Difference", "Top_scorer": "Top Scorer"}, axis=1, inplace=True)
df_copy.head()

#endregion

#region EXPORTING

# File names
csv_file = 'plf_data.csv'
excel_file = 'plf_data.xlsx'

# Export to CSV
try:
    df_copy.to_csv(csv_file, index=False)
    print(f"Data exported to {csv_file}")
except PermissionError as e:
    print(f"Permission error while writing to {csv_file}: {e}")

# Export to Excel
try:
    df_copy.to_excel(excel_file, index=False, sheet_name='2024_25 PLF Data')
    print(f"Data exported to {excel_file}")
except PermissionError as e:
    print(f"Permission error while writing to {excel_file}: {e}")

#endregion