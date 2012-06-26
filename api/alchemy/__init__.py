
import AlchemyAPI
from xml.dom.minidom import parseString

def getXMLTag(xml, tag):
    dom = parseString(xml)
    xmlTag = dom.getElementsByTagName(tag)[0].toxml()
    xmlData = xmlTag.replace('<%s>' % tag,'').replace('</%s>' % tag,'')
    
    return xmlData

alchemyObj = AlchemyAPI.AlchemyAPI()
alchemyObj.setAPIKey("896b0a964ba05c0d45ee8f882f95b8907cfb6c2d")

#result = alchemyObj.TextGetTargetedSentiment("Madonna enjoys tasty Pepsi.  I hate Madonna style.", "Pepsi");
#result = alchemyObj.TextGetTextSentiment("My name is Paul.");
#print getXMLTag(result,'type')

f = open('../test set.txt', 'r')
total = 0
count = 0
for line in f:
    total += 1
    
    tweet = line.split(' .:. ')
    sentiment = tweet[0]
    result = alchemyObj.TextGetTextSentiment(tweet[1])
    
    if sentiment == getXMLTag(result,'type').replace('negative', 'neg').replace('positive', 'pos'):
        count += 1
    else:
        print total, getXMLTag(result,'type')
        
print total, count, count/float(total) * 100