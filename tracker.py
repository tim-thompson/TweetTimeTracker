import sys

from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy


#Get String to track on
argTag = sys.argv[1]

#Class for listening to all tweets
class TweetListener(StreamListener):
    def on_status(self, status):
        print (status.created_at)

        #Write timestamp to file
        f = open("logs/" + argTag + ".txt", "a")
        f.write(str(status.created_at) + "\n")
        f.close()

        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    listener = TweetListener()

    #Keys
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    #Initialise and Authorise
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, listener)
    stream.filter(track = [argTag])
