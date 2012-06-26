from repustate import Repustate

client = Repustate(api_key='9ff89bfee51be8070baadfdda72c002e9c83de8b', version='v2')


f = open('../test set.txt', 'r')
total = 0
count = 0
for line in f:
    total += 1
    
    tweet = line.split(' .:. ')
    sentiment = tweet[0]
    result = client.sentiment(text=tweet)

    score = result['score']
    if abs(score) == 0.0:
        sentiment_label = 'neutral'
    elif score > 0:
        sentiment_label = 'pos'
    else:
        sentiment_label = 'neg'
        
        
    if sentiment == sentiment_label:
        count += 1
    else:
        print total, result['score']
        
print total, count, count/float(total) * 100