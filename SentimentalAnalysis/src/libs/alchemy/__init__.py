import AlchemyAPI
from xml.dom.minidom import parseString

def getXMLTag(xml, tag):
    dom = parseString(xml)
    xmlTag = dom.getElementsByTagName(tag)[0].toxml()
    xmlData = xmlTag.replace('<%s>' % tag,'').replace('</%s>' % tag,'')
    
    return xmlData

def classifyAlchemyAPI(text):
    alchemyObj = AlchemyAPI.AlchemyAPI()
    alchemyObj.setAPIKey("896b0a964ba05c0d45ee8f882f95b8907cfb6c2d")
    
    result = alchemyObj.TextGetTextSentiment(text)
    return {"label" : getXMLTag(result,'type').replace('negative', 'neg').replace('positive', 'pos')}