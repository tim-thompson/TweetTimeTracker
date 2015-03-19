#-*- coding: utf-8 -*-
import time
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json

#Get Hashtag to track
argTag = sys.argv[1]

#Class for listening to all tweets
class TweetListener(StreamListener):
    def on_status(self, status):
        print status.created_at

        #Write timestamp to file
        f = open("logs/" + argTag + ".txt", "a")
        f.write(str(status.created_at) + "\n")
        f.close()

        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    listener = TweetListener()

    #Keys
    CONSUMER_KEY = '7OqqdhrioufGXEvVmpwmDesos'
    CONSUMER_SECRET = 'th6XLAMDoVg6ZNE6MfGvFPmiKTcF0PaYtuv5HWOTUz3pisN0j0'
    ACCESS_KEY = '3046920851-JfLocarWiWmd8HvmSx9eYswV9cHYsj8t0bztCwL'
    ACCESS_SECRET = 'L5cyGYPB3NPhXx2Y9oDiZB02RZd7fpWuLnV2r7NPDfI6q'

    #Initialise and Authorise
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, listener)
    stream.filter(track = [argTag])
