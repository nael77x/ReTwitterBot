################################################################################
#  PLEASE DON'T CHANGR ANY COMMANDS IN THIS SCRIPT OTHERWISE IT WILL NOT WORK. #
#  AUTHOR    : PRALHAD NASANE                                                  #
#  DATE      : 03-JUNE-2020                                                    #
################################################################################
import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#########################################################################################
# Where q='#example', change #example to whatever hashtag or keyword you want to search.#
# Where items(5), change 5 to the amount of retweets you want to tweet.                 #
# Make sure you read Twitter's rules on automation - don't spammer.                     #
#########################################################################################
for tweet in tweepy.Cursor(api.search, q=('#NASA OR #ISRO -filter:retweets'), lang='en').items(5):
    try:
       
        print(colored('\nTweet by: @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.''cyan'))
        
        tweet.retweet()
        print(colored('Retweeted the tweet''green'))

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
