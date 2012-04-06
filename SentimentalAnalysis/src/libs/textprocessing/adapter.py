# To use the Text-Processing API in your code, just import the generated code
# add your developer key (you can find it in your dashboard: http://www.mashape.com/account/index )
# and relax!
# This is a sample of the initialization of the client.. then call its methods!

from libs.textprocessing.TextProcessing import TextProcessing 
import util

def query(text):
    if not text:
        return None
    
    obj = TextProcessing("PUBqD=D4=4KKr4WvOfxh#VMkayw$W-iO", "PRI-@KOUBovv#gV-cPGC3wd$%P2fYU3k")
    
    try:
        return obj.sentiment(util.remover_acentos(text))
    except Exception:
        return {'label' : 'erro'}