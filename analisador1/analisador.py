#coding=UTF-8

#!/usr/bin/python 
#
# wget wget http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6010/zip/imm6010.zip
# unzip imm6010.zip
#
# Aqui: http://fnielsen.posterous.com/simplest-sentiment-analysis-in-python-with-af

import math
import re
import sys
reload(sys)
#sys.setdefaultencoding('utf-8')

# AFINN-111 is as of June 2011 the most recent version of AFINN
filenameAFINN = 'AFINN/AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))

# Word splitter pattern
pattern_split = re.compile(r"\W+")

def sentiment(text):
    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence. 
    """
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
        
#        print sentiment, text
    else:
        sentiment = 0
        
    if sentiment < 0:
        return 'negative'
    elif sentiment == 0:
        return 'neutral'
    elif sentiment > 0:
        return 'positive'
    


if __name__ == '__main__':
    # Single sentence example:
    text = "Finn is a ugly guy"
    print("%6.2f %s" % (sentiment(text), text))
    
    # No negation and booster words handled in this approach
    text = "Americans to Support Strike Against Iran if Nuclear Claims Proven - IF YOU WANT WAR WITH IRAN AMERICA - SEND YOUR OWN KIDS AND THEN YOU WILL..."
    print("%6.2f %s" % (sentiment(text), text))
    
    # No negation and booster words handled in this approach
    text = "'The dangers of carbon dioxide? Tell that to a plant, how dangerous carbon dioxide is.'--Rih Santorum"
    print("%6.2f %s" % (sentiment(text), text))
    
    # Example with downloading from Twitter:
#    import simplejson 
#    import urllib
#
#    query = "Romney"
#    json = simplejson.load(urllib.urlopen("http://search.twitter.com/search.json?q=" + query))
#    sentiments = map(sentiment, [ tweet['text'] for tweet in json['results'] ])
#    print("%6.2f %s" % (sum(sentiments)/math.sqrt(len(sentiments)), query))