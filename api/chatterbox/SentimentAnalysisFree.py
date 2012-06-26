import sys
sys.path.append("mashape")

from mashape.http.http_client import HttpClient 

class SentimentAnalysisFree:
	def __init__(self, publicKey, privateKey):
		self.publicKey = publicKey
		self.privateKey = privateKey

	def classifytext(self, lang, text, exclude = None, mashape_callback=None):
		parameters = {"lang" : lang,
		              "text" : text,
		              "exclude" : exclude}
		mashape_client = HttpClient()
		response = mashape_client.do_call("POST", "http://free-dev.cbanalytics.co.uk/sentiment/current/classify_text/", parameters, True, self.publicKey, self.privateKey, mashape_callback, True)
		return response
