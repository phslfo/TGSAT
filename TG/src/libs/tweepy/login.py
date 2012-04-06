'''
Created on 14/03/2012

@author: Paulo Oliveira
'''
import tweepy

def login():
    consumer_key="sOoc9GLBXJedKQkkEnaX3Q"
    consumer_secret="bkGV1Hky9iRuNl2lvTl3kUR79mQNTcfv4s1zcGY"
    
    # The access tokens can be found on your applications's Details
    # page located at https://dev.twitter.com/apps (located
    # under "Your access token")
    access_token="141296799-MKkHIYdlXDvvICeIhwNHEdGq45ZOBnZZjTtueVrp"
    access_token_secret="t9YBdErTlkWAjXEiLpAOel9EFR79IrWzY315xDNi4xg"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    return auth