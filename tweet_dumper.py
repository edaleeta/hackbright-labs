#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import os

#Twitter API credentials
consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_key = os.environ['TWITTER_ACCESS_TOKEN_KEY']
access_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


def get_tweets(screen_names):
    tweet_files = []
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    for user in screen_names:
        #initialize a list to hold all the tweepy Tweets
        alltweets = []

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=user, count=100)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [tweet.text.encode("utf-8") for tweet in alltweets]

        twitter_text = " ".join(outtweets)

        #write the csv
        with open('%s_tweets.txt' % user, 'w') as f:
            f.write(twitter_text)

        tweet_files.append('{}_tweets.txt'.format(user))

    return tweet_files

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("beccamoss")
