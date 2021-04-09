##IMPORTS##############################################################################
import twitter
import disquette
import time
from api import *
##SOME KEYS############################################################################
user_naima = 1272625686776348673
user_matteo = 1041584119313047557
user_paul = 3218510620
user_fandenaima = 1126536603869093888
##API##################################################################################
api = twitter.Api(consumer_key=api_key,
                  consumer_secret=api_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)
##FUNCTIONS############################################################################

def get_last_tweets(user,count=5) :
    return api.GetUserTimeline(user_id=user,count=count,include_rts=False,exclude_replies=True)

def post_reply(tweet,text):
    tid = tweet.id
    content = tweet.text
    author = tweet.user.screen_name
    new_text = "@"+author+" "+text
    new_text = new_text[:280]
    print(f"Posting a reply to the tweet id : {tid} ; text : {content}")
    api.PostUpdate(status=new_text,in_reply_to_status_id=tid)
    print(f"Replied : {text}")

def wait_for_a_tweet(user,sleep_time=60):
    seen_tweets = get_last_tweets(user,10)
    seen_tweets_text = [s.text for s in seen_tweets]
    
    last_tweet = get_last_tweets(user,1)
    new_last_tweet = get_last_tweets(user,1)
    while last_tweet == new_last_tweet or new_last_tweet == [] or new_last_tweet[0].text in seen_tweets_text :
        print("...")
        time.sleep(sleep_time)
        last_tweet = new_last_tweet
        new_last_tweet = get_last_tweets(user,1)

    tweet = new_last_tweet[0]
    print(f"The user {user} has twitted \"{tweet.text}\" !")
    return tweet

def kind_messages_to(user,sleep_time=60):
    try:
        while True:
            tweet = wait_for_a_tweet(user,sleep_time)
            disk = disquette.get_unique_disquette()
            post_reply(tweet,disk)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__" :
    kind_messages_to(user_fandenaima,10)