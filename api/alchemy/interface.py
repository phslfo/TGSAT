from alchemy import getXMLTag, AlchemyAPI

alchemyObj = AlchemyAPI.AlchemyAPI()
alchemyObj.setAPIKey("896b0a964ba05c0d45ee8f882f95b8907cfb6c2d")

def classifyAlchemyAPI(text):
    result = alchemyObj.TextGetTextSentiment(text)
    return getXMLTag(result,'type').replace('negative', 'neg').replace('positive', 'pos')