


f = open('../test set.txt', 'r')
from lymbix import Lymbix

lymbix = Lymbix('c6a2c5af610c650d2db35a98ab922741618b734e')    
    
#rdata = lymbix.tonalize("My name is Paul.")
#print rdata['article_sentiment']

total = 0
count = 0
for line in f:
    total += 1
    
    tweet = line.split(' .:. ')
    sentiment = tweet[0]
    result = lymbix.tonalize(tweet[1])    
    
#    if sentiment == result['article_sentiment']['sentiment'].lower().replace('negative', 'neg').replace('positive', 'pos'):
#        count += 1
#    else:
#        print total, result['article_sentiment']
    
    score = result['article_sentiment']['score']
    if abs(score) < 0.25:
        sent_temp = 'neutral'
    elif score > 0:
        sent_temp = 'pos'
    else:
        sent_temp = 'neg'
        
    if sentiment == sent_temp:
        count += 1
    else:
        print total, result['article_sentiment']
        
    import time
    time.sleep(1)     
        
print total, count, count/float(total) * 100