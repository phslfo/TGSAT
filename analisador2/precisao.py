from analisador import Classificador

f = open('C:\Users\Paulo Oliveira\Desktop\\teste feats.txt', 'r')
count = 0
total = 0
c = Classificador(False, False, False, True)

for l in f:
    total += 1
    data = l.split(' .:. ') 
    
    try:
        sentiment = c.analisar2(data[1])
        
        if sentiment['label'] == data[0]:
            count += 1
        else:
#            pass
            print total, sentiment['prob'], sentiment['label'], data[1].strip()
    except Exception, e:
        print e
        break
    
print total, count, count/float(total) * 100