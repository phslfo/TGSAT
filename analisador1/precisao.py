import analisador

f = open('C:\Users\Paulo Oliveira\Desktop\\teste feats.txt', 'r')
count = 0
total = 0
for l in f:
    total += 1
    data = l.split('.:.') 
    
    try:
        sentiment = analisador.sentiment(data[1])
        
        if sentiment['label'] == data[0].strip():
            count += 1
        else:
            print sentiment['prob'], data[0].strip(), data[1].strip()
    except:
        continue
    
print total, count, count/float(total) * 100