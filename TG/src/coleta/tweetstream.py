#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Quick example of using OAuth and the Streaming interface with a Geographic
bounding box and optionally an additional query filter.

"""

from libs import tweepy
from libs.tweepy.streaming import StreamListener, Stream

class Listener ( StreamListener ):
    
    count = 0
    
    def on_status( self, status ):
        separator = '~@~'
        
        f = open('data/base.txt', 'a')
        f.write(
                str(status.author.id)+ separator +
                str(status.author.name)+ separator +
                str(status.author.screen_name) + separator + 
                str(status.id) + separator +
                str(status.text) + separator + 
                str(status.author.location) + separator + 
                str(status.place['full_name'] if status.place else 'None') + separator + 
                str(status.created_at) + '\n'
                )
        f.close()  
        
        if self.count + 12748 == 20000:
            exit()
        
        self.count += 1
        print self.count
        
        return
    
    def on_error(self, status_code):
        if status_code != 406:
            print 'An error has occured! Status code = %s' % status_code
        else:
            print 'Error: 406, It is possible that your bounding box is ' \
                  'not SouthWest longitude, SouthWest latitude, NorthEast ' \
                  'longitude, Northeast Latitude'
        return True
    
    def on_timeout(self):
        return True
 
def main():
    """
Go to:

https://dev.twitter.com/apps/new

Create an app, agree to the terms, Create your access token (you may need
to reload the page).

Replace the CONSUMER KEY, CONSUMER SECRET, ACCESS TOKEN and ACCESS TOKEN
SECRET with the values generated from the
https://dev.twitter.com/apps/xxxxxx/show page

You don't need to give the app write privileges as it is only
going to follow the stream and print the messages within the bounding
box.

"""

    consumer_key="sOoc9GLBXJedKQkkEnaX3Q"
    consumer_secret="bkGV1Hky9iRuNl2lvTl3kUR79mQNTcfv4s1zcGY"
    access_token="141296799-MKkHIYdlXDvvICeIhwNHEdGq45ZOBnZZjTtueVrp"
    access_token_secret="t9YBdErTlkWAjXEiLpAOel9EFR79IrWzY315xDNi4xg"

    auth1 = tweepy.auth.OAuthHandler(consumer_key,consumer_secret)
    auth1.set_access_token(access_token,access_token_secret)
#    api = tweepy.API(auth1)
 
    listener = Listener()
    stream = Stream(auth=auth1, listener=listener, timeout=None,)
 
    # filter messages from Florida and part of Georgia using two bounding
    # boxes
#    stream.filter(locations=[
#         -87.528076,29.363027,-81.210937,30.836215,
#         -82.825928,24.417142,-79.94751,29.363027,
#    ])

    #filter messages with the text 'apple'
    stream.filter(None,['Santorum', 'Romney', '#santorum', '#romney'])

if __name__ == '__main__':
    try:
        main() 
    except KeyboardInterrupt:
        print '\nGoodbye!'