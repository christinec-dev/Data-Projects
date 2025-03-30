# Imports
import os
import praw
import pandas as pd
import numpy as np
import time
from dotenv import load_dotenv
from textblob import TextBlob

#region EXTRACTION

# Load environment variables from .env file
load_dotenv()

# Reddit API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# Access the AITA subreddit
subreddit_name = 'confession'
subreddit = reddit.subreddit(subreddit_name)

# Scrape top posts from the subreddit
posts_data = []
for submission in subreddit.top(limit=50):  # Limit to the top 50 posts
    # Delay between requests to avoid rate limiting
    time.sleep(2)
    # Load all comments
    submission.comments.replace_more(limit=0)
    
    # Filter posts based on tags
    tags = submission.link_flair_text
    if tags not in ['META']:
        post_info = {
            "url": submission.url,
            "timestamp": submission.created_utc,
            'author': submission.author.name if submission.author else 'Unknown',
            "title": submission.title,
            "story": submission.selftext,
            "upvotes": submission.score,
            "comment_count": submission.num_comments
        }
        posts_data.append(post_info)

# Convert to DataFrame
df = pd.DataFrame(posts_data)

# Get user activity
def get_user_activity(username):
    try:
        user = reddit.redditor(username)
        submissions = list(user.submissions.new(limit=None))  # Fetch all submissions
        comments = list(user.comments.new(limit=None))  # Fetch all comments
        
        # Calculate activity metrics
        author_submissions = len(submissions)
        author_comments = len(comments)
        
        return author_submissions, author_comments
    except Exception as e:
        # Return default values for private or inaccessible profiles
        return 1, 0

# Add user activity data to the DataFrame
df[['author_submissions', 'author_comments']] = df['author'].apply(
    lambda x: get_user_activity(x) if x != 'Unknown' else (None, None)
).apply(pd.Series)

# Add word count
df['word_count'] = df['story'].apply(lambda x: len(x.split()))

# Add unique word count
df['unique_word_count'] = df['story'].apply(lambda x: len(set(x.split())))

# Add character count
df['character_count'] = df['story'].apply(lambda x: len(x))

# Add sentiment analysis
df['sentiment'] = df['story'].apply(lambda x: TextBlob(x).sentiment.polarity)

#endregion

#region PREPROCESSING

# Replace missing values
df["author_submissions"] = df["author_submissions"].fillna(1) # since they made 1 post
df["author_comments"] = df["author_comments"].fillna(0)

# Rename columns
df_copy = df.copy()
df_copy.columns = df_copy.columns.str.capitalize()
df_copy.rename({"Comment_count": "Comment Count", "Url": "URL", "Author_submissions": "Author Submissions", "Author_comments": "Author Comments", "Word_count": "Word Count", "Unique_word_count": "Unique Word Count", "Character_count": "Character Count"}, axis=1, inplace=True)

#endregion

#region EXPORTING

# File names
csv_file = 'reddit_confessions_data.csv'
excel_file = 'reddit_confessions_data.xlsx'

# Export to CSV
try:
    df_copy.to_csv(csv_file, index=False)
    print(f"Data exported to {csv_file}")
except PermissionError as e:
    print(f"Permission error while writing to {csv_file}: {e}")

# Export to Excel
try:
    df_copy.to_excel(excel_file, index=False, sheet_name='Top 50 rconfessions Data')
    print(f"Data exported to {excel_file}")
except PermissionError as e:
    print(f"Permission error while writing to {excel_file}: {e}")

#endregion