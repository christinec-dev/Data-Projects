# Imports
import requests
import numpy as np
import pandas as pd
import re

#region EXTRACTION

# Id of game we want to get reviews from (Balders gate 3)
app_id = 1086940

# Get 50 reviews from users
def fetch_user_reviews(app_id, day_range):
    params = {
        "json": 1,
        "language": "english",
        "num_per_page": 50,
        "review_type": "all",
        "purchase_type": "steam",
        "day_range": day_range
    }
    all_url = f"https://store.steampowered.com/appreviews/{app_id}"
    all_response = requests.get(all_url, params=params)
    all_data = all_response.json()
    reviews_list = all_data.get("reviews", [])
    return pd.DataFrame(reviews_list)

# Fetch reviews from different time periods
df_early_access = fetch_user_reviews(app_id, 365 * 5)  # 5 years ago
df_just_released = fetch_user_reviews(app_id, 365 * 2)  # 2 years ago
df_recent = fetch_user_reviews(app_id, 60)  # last 60 days
df_early_access['Review Timeframe'] = 'Early Access'
df_just_released['Review Timeframe'] = 'Beta Release'
df_recent['Review Timeframe'] = 'Alpha Release'
df_users = pd.concat([df_early_access, df_just_released, df_recent], ignore_index=True)
df_users['Type'] = 'User'

# Get 50 reviews from curators
def fetch_curator_reviews(app_id, day_range):
    params = {
        "json": 1,
        "language": "english",
        "num_per_page": 50,
        "review_type": "all",
        "purchase_type": "non_steam_purchase",
        "day_range": day_range
    }
    all_url = f"https://store.steampowered.com/appreviews/{app_id}"
    all_response = requests.get(all_url, params=params)
    all_data = all_response.json()
    reviews_list = all_data.get("reviews", [])
    return pd.DataFrame(reviews_list)

# Fetch reviews from different time periods
df_early_access = fetch_curator_reviews(app_id, 365 * 5)  # 5 years ago
df_just_released = fetch_curator_reviews(app_id, 365 * 2)  # 2 years ago
df_recent = fetch_curator_reviews(app_id, 60)  # last 60 days
df_early_access['Review Timeframe'] = 'Early Access'
df_just_released['Review Timeframe'] = 'Beta Release'
df_recent['Review Timeframe'] = 'Recent'
df_curators = pd.concat([df_early_access, df_just_released, df_recent], ignore_index=True)
df_curators['Type'] = 'Curator'

# Combine the data
df = pd.concat([df_users, df_curators])

#endregion

#region PREPROCESSING

# Drop redundant columns
df_copy = df.copy()
df_copy = df_copy.drop(['comment_count', 'votes_funny', 'primarily_steam_deck', 'language', 'received_for_free', 'timestamp_updated', 'written_during_early_access'], axis=1)

# Extract values from the author column
df_copy['num_reviews'] = df_copy['author'].apply(lambda x: x['num_reviews'] if isinstance(x, dict) else None)
df_copy['playtime_at_review'] = df_copy['author'].apply(lambda x: x['playtime_at_review'] if isinstance(x, dict) else None)
df_copy['Author ID'] = df_copy['author'].apply(lambda x: x['steamid'] if isinstance(x, dict) else None)
df_copy['Recommendation'] = df_copy['voted_up'].apply(lambda x: 'Recommended' if x else 'Not Recommended')
df_copy = df_copy.drop(['author'], axis=1)
df_copy = df_copy.drop(['voted_up'], axis=1)

# Text handling
pattern = r'[^\w\s]'
df_copy['review'] = df_copy['review'].apply(lambda x: re.sub(pattern, '', x))

# Rename columns
df_copy.columns = df_copy.columns.str.capitalize()
df_copy.rename({"Recommendationid": "Review ID", "Timestamp_created": "Created At", "Review timeframe": "Review Timeframe", "Votes_up": "Upvotes", "Weighted_vote_score": "Weighted Score", "Steam_purchase": "Purchased", "Written_during_early_access": "Early Access", "Num_reviews": "Reviews Written", "Playtime_at_review": "Playtime At Review", "Author id": "Author ID"}, axis=1, inplace=True)

# Reformat dataframe
df_copy = df_copy.reindex(columns=['Review ID', 'Author ID', 'Type', 'Reviews Written', 'Playtime At Review', 'Recommendation', 'Review', 'Weighted Score', 'Upvotes', 'Purchased', 'Review Timeframe', 'Created At'])
df_copy = df_copy.sample(frac=1).reset_index(drop=True)

#endregion

#region EXPORTING

# File names
csv_file = 'baldurs_gate_3_data.csv'
excel_file = 'baldurs_gate_3_data.xlsx'

# Export to CSV
try:
    df_copy.to_csv(csv_file, index=False)
    print(f"Data exported to {csv_file}")
except PermissionError as e:
    print(f"Permission error while writing to {csv_file}: {e}")

# Export to Excel
try:
    df_copy.to_excel(excel_file, index=False, sheet_name='Steam Reviews')
    print(f"Data exported to {excel_file}")
except PermissionError as e:
    print(f"Permission error while writing to {excel_file}: {e}")

#endregion