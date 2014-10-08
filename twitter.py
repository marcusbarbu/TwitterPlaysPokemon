import twython
from twython import TwythonStreamer
import collections
import time
from Counter import Counter

#oauth stuff
app_key = ""
app_secret = ""
my_key = ""
my_secret = ""
#variables
tweets = []
number = 0
tweet_limit = 40


#define streamer class
class Streamer(TwythonStreamer):
    def on_success(self, data):
        #debugging
        #print "done"
        #make vars global
        global tweets, tweet_limit, number
        #pull tweets, counter used to limit data
        if 'text' in data and number <= tweet_limit:
            tweets.append(data['text'].encode('utf-8'))
            number+=1
        else:
            self.disconnect()
    '''def on_success(self,data):
        print 'y'
        return data'''
    def on_error(self, status_code, data):
        print status_code
        print "oh shit"
        time.sleep(5)
        
    '''def get_tweets(self,data):
        print 'x'
        global number, tweets, tweet_limit
        if 'text' in data and number <= tweet_limit:
            tweets.append(data['text'].encode('utf-8'))
            number += 1
            print done
        else:
            return tweets'''

        

class TweetBuffer:
    def __init__(self):
        self.button = ""
        self.filtered_text = ""
        
    def get_tweets(self):
        stream = Streamer(app_key,app_secret,my_key,my_secret)
        stream.statuses.filter(track = "twitter")
        text = "".join(tweets)
        self.filtered_text = text.lower()
        
    def compute(self):
        counter = Counter(self.filtered_text)
        counter.count()
        counter.get_button()
        
        self.button = counter.compare_str
        
    def reset(self):
        global tweets, number
        tweets = []
        number = 0
        time.sleep(1)
'''
while True:
    stream = Streamer(app_key,app_secret,my_key,my_secret)
    #print '1'
    stream.statuses.filter(track = "twitter")
    #print '2'
    #stream.get_tweets(stream.statuses.filter(track = 'twitter'))
    #print '3'
    text = "".join(tweets)
    filtered_text = text.lower()
    
    counter = Counter(filtered_text)
    
    counter.count()
    counter.get_button()
    print counter.d
    print counter.button_dict
    print counter.compare_val
    #print counter.up
    print counter.compare_str
    #time.sleep(1)"""
    #print counter.get_button()
    tweets = []
    number = 0
    time.sleep(2) '''

'''for i in range(10):
    tweet = TweetBuffer()
    tweet.get_tweets()
    tweet.compute()
    print tweet.button
    tweet.reset()'''

class TwitterProcess:
    def __init__(self):
        self.button = ''

    def cycle(self):
        tweet = TweetBuffer()
        tweet.get_tweets()
        tweet.compute()
        self.button = tweet.button
        tweet.reset()
