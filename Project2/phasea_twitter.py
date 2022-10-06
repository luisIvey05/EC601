import tweepy
import configparser
import requests
import botometer

USERID = 'elonmusk'
SEARCHQUERY = "#Waymo"
# READ CONFIGS
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']
rapid_api_key = config['twitter']['rapid_api_key']

# AUTHENTICATION
client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=api_key,
                       consumer_secret=api_key_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       return_type=requests.Response,
                       wait_on_rate_limit=True)

# MAKE A SEARCH QUERY
query = 'from: elonmusk'
personal_tweets = client.search_recent_tweets(query=query,
                                    tweet_fields=['author_id', 'created_at'],
                                    max_results=10)

tweet_dict = personal_tweets.json()
print(tweet_dict)

# SEARCH QUERY BASED ON A PERIOD IN TIME
query = "#covid19 lang:en -is:retweet"
start_time = "2022-09-30T00:00:00Z"
end_time = "2022-10-01T00:00:00Z"

tweets = client.search_recent_tweets(query=query,
                                     start_time=start_time,
                                     end_time=end_time,
                                     tweet_fields = ["created_at", "text", "source"],
                                     user_fields = ["name", "username", "location", "verified", "description"],
                                     max_results = 10,
                                     expansions='author_id'
                                     )
tweets_dict = tweets.json()
print(tweets_dict)


twitter_app_auth = {
    'consumer_key': api_key,
    'consumer_secret': api_key_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapid_api_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@elonmusk')
print(result)