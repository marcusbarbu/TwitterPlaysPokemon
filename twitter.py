import twython
from twython import TwythonStreamer
import collections
import time
from Counter import Counter

#oauth stuff

#variables
tweets = []
number = 0
tweet_limit = 40
finished = False


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

    def on_error(self, status_code, data):
        print status_code
        #print "oh shit"
        time.sleep(5)

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

class TwitterProcess:
    def __init__(self):
        self.button = ''


    def cycle(self):
        self.tweet = TweetBuffer()
        self.tweet.get_tweets()
        self.tweet.compute()
        self.button = self.tweet.button
        self.tweet.reset()
