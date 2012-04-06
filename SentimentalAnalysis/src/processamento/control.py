from string import punctuation
from libs import textprocessing
import socket
import util
import threading
import time

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

def analise(tweets_list, my_queue):
    for tweet in tweets_list:
        text_without_accents = util.remover_acentos(tweet['text'])
        
        if text_without_accents:        
            analise1 = textprocessing.adapter.query(text_without_accents) 
            analise2 = analyse2(text_without_accents) 
            analise3 = analyse3(text_without_accents) 
        
            my_queue.put((tweet, analise1, analise2, analise3))
        
        else:
            my_queue.put((tweet, {'label' : 'erro'}, 'erro', 'erro'))

def analysis_sentimental(tweets_list, d1=True, d2=True, d3=True):    
    from Queue import Queue 
    my_queue = Queue()

    meio = len(tweets_list)/2
    
    t1 = threading.Thread(name='t1', target=analise, args=(tweets_list[0:meio], my_queue,))
    t2 = threading.Thread(name='t2', target=analise, args=(tweets_list[meio:], my_queue,))    
    t1.start()
    t2.start()
    
    
    while t1.isAlive() or t2.isAlive():
        time.sleep(10)
    
    lista = [my_queue.get() for i in range(my_queue.qsize())]
    
    return lista

#def analysis_sentimental(tweets_list, d1=True, d2=True, d3=True):
#        
#    lista = []
#    for tweet in tweets_list:
#        analise1 = textprocessing.adapter.query(util.remover_acentos(tweet['text'])) if d1 else {'label' : 'nada'}
#        analise2 = analyse2(util.remover_acentos(tweet['text'])) if d2 else "nada"
#        analise3 = analyse3(util.remover_acentos(tweet['text'])) if d3 else "nada"
#        
#        lista.append((tweet, analise1, analise2, analise3))
#
#    return lista

def analyse2(text):

    HOST = 'localhost'    # The remote host
    PORT = 7001           # The same port as used by the server
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(text)
        data = s.recv(1024)
        s.close()
    except Exception:
        return "erro"
    
    return repr(data)

def analyse3(text):

    HOST = 'localhost'    # The remote host
    PORT = 7002           # The same port as used by the server
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(text)
        data = s.recv(1024)
        s.close()
    except Exception:
        return "erro"
    
    return repr(data)