# Collect tweets by words
import os
import tweepy as tw
import pandas as pd
#Add secret keys
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


search_words = ""
date_since = "2018-11-11"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(100)

# Iterate and print tweets
with open(search_words+".txt","w") as file:
    for tweet in tweets:
        file.write(str(tweet.text))
        file.write("\n")
        file.write("\n")

        print(tweet.text)
    
