import tweepy
import time
import wget
import os
from datetime import datetime



consumer_key = #insert
consumer_secret = #insert
key = #insert
secret = #insert

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'
media_files = set()


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    userID = "realDonaldTrump"
    tweets = api.user_timeline(screen_name=userID, since_id = read_last_seen(FILE_NAME), tweet_mode = 'extended', include_rts = False)

    for tweet in reversed(tweets) :

        media_caught = False

        #Checks if tweet contains a media, and downloads it if media exists.
        media = tweet.entities.get('media',[])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
        for media_file in media_files:
            downloaded_file = wget.download(media_file)
            media_caught = True


        print("Catching Tweet")
        time.sleep(0.3)
        print("Catching Tweet.")
        time.sleep(0.3)
        print("Catching Tweet..")
        time.sleep(0.3)
        print("Catching Tweet...")
        time.sleep(0.3)

        #Removes media links from text
        sep = 'https://t.co'
        tweet.full_text = tweet.full_text.split(sep, 1)[0]

        #Yells tweet
        if media_caught:
            api.update_with_media(downloaded_file, tweet.full_text.upper())
            os.remove(downloaded_file)
        else:
            api.update_status(tweet.full_text.upper())
        store_last_seen(FILE_NAME, tweet.id)

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y at %H:%M:%S")
        print("Trump has yelled the " + dt_string)


while True:
    reply()
    time.sleep(20)
