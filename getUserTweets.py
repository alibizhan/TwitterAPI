import tweepy
import sys
import os
from dotenv import load_dotenv
import csv
import re

# Load credentials from .env file
load_dotenv()

#https://stackoverflow.com/a/49986645/3711660

def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


# 1. Authenticate
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'),os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'),os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

if (not api):
    print("Authentication failed!")
    sys.exit(-1)

# 2. Get data
userName = "binance"
data = api.user_timeline(userName, tweet_mode="extended",count=1000)

# 3. Save data
with open(userName+'.csv', mode='w', encoding='utf-8', newline='') as file:
    columns = ['Date', 'Tweet']
    writer = csv.DictWriter(file, columns)
    writer.writeheader()

    for i in data:
        writer.writerow({'Tweet': deEmojify(i.full_text),'Date': i.created_at})

print('DONE!')