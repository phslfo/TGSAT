#coding=UTF-8

import util
from realtime import control
import processamento

def realtime(request):
    if request.method == 'GET':
        query = request.GET.get('q', None)
        
        if query:
            tweets = control.get_realtime_tweets(query + " -RT")
            
            tweets_analysed = processamento.control.analysis_sentimental(tweets)
            top_words = processamento.control.top_words(tweets)
            top_hashtags = processamento.control.top_hashtags(tweets)
            top_users = processamento.control.top_users(tweets)
            
            d = {
                 'tweets'       : tweets_analysed,
                 'top_words'    : top_words,
                 'top_hashtags' : top_hashtags,
                 'top_users'    : top_users
                 }
            
            return util.request.render('realtime.html', d, request)
        
        else:
            print 'Nenhuma query enviada!'