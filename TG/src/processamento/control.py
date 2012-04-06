from string import punctuation
from libs import textprocessing
import socket

ignore_words = ['the', 'this', 'that', 'for', 'and']

def top_words(tweets_list, number=10):
    words = {}    
    words_gen = (word.strip(punctuation).lower() for tweet in tweets_list
                                                 for word in tweet['text'].split()
                                                    if len(word) >= 3 and word not in ignore_words)
    
    for word in words_gen:
        words[word] = words.get(word, 0) + 1
    
    top_words = sorted(words.iteritems(),
                       cmp=lambda x, y: cmp(x[1], y[1]) or cmp(y[0], x[0]),
                       reverse=True)[:number]
    
    return top_words

def top_hashtags(tweets_list, number=10):
    words = {}    
    words_gen = (word.strip().lower() for tweet in tweets_list
                                                 for word in tweet['text'].split()
                                                    if word.startswith('#'))
    
    for word in words_gen:
        words[word] = words.get(word, 0) + 1
    
    top_hashtags = sorted(words.iteritems(),
                       cmp=lambda x, y: cmp(x[1], y[1]) or cmp(y[0], x[0]),
                       reverse=True)[:number]
    
    return top_hashtags

def top_users(tweets_list, number=10):
    words = {}    
    words_gen = (tweet['user'] for tweet in tweets_list)
    
    for word in words_gen:
        words[word] = words.get(word, 0) + 1
    
    top_users = sorted(words.iteritems(),
                       cmp=lambda x, y: cmp(x[1], y[1]) or cmp(y[0], x[0]),
                       reverse=True)[:number]
    
    return top_users

def analysis_sentimental(tweets_list):
        
    lista = []
    for tweet in tweets_list:
        analise1 = {'label' : 'porra'}
#        analise1 = textprocessing.adapter.query(tweet['text'])
        analise2 = analyse1(tweet['text'])
        analise3 = analyse2(tweet['text'])
        lista.append((tweet, analise1, analise2, analise3))

    return lista

def analyse1(text):

    HOST = 'localhost'    # The remote host
    PORT = 7001           # The same port as used by the server
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(text)
    data = s.recv(1024)
    s.close()
    
    return repr(data)

def analyse2(text):

    HOST = 'localhost'    # The remote host
    PORT = 7002           # The same port as used by the server
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(text)
    data = s.recv(1024)
    s.close()
    
    return repr(data)