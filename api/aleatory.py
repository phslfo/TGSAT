import random

f = open('test set.txt', 'r')
total = 0
count = 0
for line in f:
    total += 1
    
    tweet = line.split(' .:. ')
    sentiment = tweet[0]
    
    if sentiment == random.choice(['pos', 'neutral', 'neg']):
        count += 1
        
print total, count, count/float(total) * 100