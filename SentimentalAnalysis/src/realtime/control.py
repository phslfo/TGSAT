#coding=UTF-8

from libs import tweepy
from realtime.models import Tweet, User
import datetime
#you know rick santorum running for pres actually makes me faithful in the fact that basically anyone can fucking run / AdventureTeamX / 
fake_list = [
            {'user_id': u'480380502', 'image': u'https://si0.twimg.com/profile_images/1891700718/image_normal.jpg', 'tweet_id': u'179925441853915136', 'user': u'CuupermaxMarco', 'date': datetime.datetime(2012, 3, 14, 13, 42, 22), 'text': u'If #Santorum becomes the republican candidate for the #uselection the republican party will lose'}, 
            {'user_id': u'56798817', 'image': u'https://si0.twimg.com/profile_images/510982282/icon_normal.jpg', 'tweet_id': u'179925403819974656', 'user': u'poorservant', 'date': datetime.datetime(2012, 3, 14, 13, 42, 13), 'text': u'RT @CatholicLisa http://t.co/QcrEsJBr #Santorum opens big lead in #Pennsylvania @RickSantorum #PA #politics #news #tcot #teaparty #gop #2012'},
            {'user_id': u'480380502', 'image': u'https://si0.twimg.com/profile_images/1891700718/image_normal.jpg', 'tweet_id': u'179925441853915136', 'user': u'CuupermaxMarco', 'date': datetime.datetime(2012, 3, 14, 13, 42, 22), 'text': u'#Santorum is like the race car driver who is down 1 lap and blocking his teammate who is currently running in 1st place.#Romney'}, 
            {'user_id': u'56798817', 'image': u'https://si0.twimg.com/profile_images/436378567/UHFinal1_normal.jpg', 'tweet_id': u'179925403819974656', 'user': u'poorservant', 'date': datetime.datetime(2012, 3, 14, 13, 42, 13), 'text': u'Also FUCK Rick Santorum. Racist fuck.'},
            {'user_id': u'480380502', 'image': u'https://si0.twimg.com/profile_images/1891700718/image_normal.jpg', 'tweet_id': u'179925441853915136', 'user': u'CuupermaxMarco', 'date': datetime.datetime(2012, 3, 14, 13, 42, 22), 'text': u'If Santorum lost his home state it would be very embarrassing. Romney has won all 5 of his home states.'}, 
            {'user_id': u'56798817', 'image': u'https://si0.twimg.com/profile_images/436378567/UHFinal1_normal.jpg', 'tweet_id': u'179925403819974656', 'user': u'poorservant', 'date': datetime.datetime(2012, 3, 14, 13, 42, 13), 'text': u'Problems With the Truth: Confessions of a 22-Year Rick Santorum Observer - Forbes http://t.co/npMficHw'},
            {'user_id': u'56798817', 'image': u'https://si0.twimg.com/profile_images/436378567/UHFinal1_normal.jpg', 'tweet_id': u'179925403819974656', 'user': u'poorservant', 'date': datetime.datetime(2012, 3, 14, 13, 42, 13), 'text': u'@faithsone ㅋㅋㅋ u so smart & progressive. i thou\'ght u were like @moontoseu or rick santorum ^^;'},
        ]
 
def get_realtime_tweets(query, size=500, get_realtime=True):
    
    if not get_realtime:
        return fake_list
   
    api = tweepy.API()
   
    tweets = []
    for status in tweepy.Cursor(api.search, q=query, rpp=100, lang="en").items(size):
        #for status in page:
            d = {
                    'user'      : status.from_user,
                    'user_id'   : status.from_user_id_str,
                    'image'     : status.profile_image_url_https,
                    'text'      : status.text.replace('\r', '').replace('\n', ''),
                    'tweet_id'  : status.id_str,
                    'date'      : status.created_at
                    }
            
#            u = User.new(d['user_id'], d['user'], d['image'])
#            u.save()
#            t = Tweet.new(d['tweet_id'], d['text'], d['date'], u)
#            t.save()     
            
            tweets.append(d)
                    
    return tweets
