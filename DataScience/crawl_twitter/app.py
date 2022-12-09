import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

api = tweepy.API(auth, wait_on_rate_limit=True)


print("###############################get user data##########################")


def get_user_data(api, username):
    try:
        user = api.get_user(screen_name=username)
        print(user.screen_name)
        print(user.followers_count)
        for friend in user.friends():
            print(friend.screen_name)
    except:
        pass


get_user_data(api, "twitter")

print("###############################search data##########################")

search_words = "#job data science"
date_since = "2018-11-16"
tweets = tweepy.Cursor(api.search_tweets,
                       q=search_words,
                       lang="en",
                       ).items(5)
for tweet in tweets:
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("text: ", tweet.text)
    print("user: ", tweet.user.screen_name)
    print("location: ", tweet.user.location)
    print("+++++++++++++++++++++++++++++++++++++++++")
