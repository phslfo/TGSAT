# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '1.8'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from libs.tweepy.models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResult, ModelFactory
from libs.tweepy.error import TweepError
from libs.tweepy.api import API
from libs.tweepy.cache import Cache, MemoryCache, FileCache
from libs.tweepy.auth import BasicAuthHandler, OAuthHandler
from libs.tweepy.streaming import Stream, StreamListener
from libs.tweepy.cursor import Cursor 

# Global, unauthenticated instance of API
api = API()

def debug(enable=True, level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level

