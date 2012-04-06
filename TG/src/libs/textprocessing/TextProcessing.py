import sys
sys.path.append("mashape")

from mashape.http.http_client import HttpClient

class TextProcessing:
	def __init__(self, publicKey, privateKey):
		self.publicKey = publicKey
		self.privateKey = privateKey

	def phrases(self, text, language, mashape_callback=None):
		parameters = {"text" : text,
		              "language" : language}
		mashape_client = HttpClient()
		response = mashape_client.do_call("POST", "http://api.text-processing.com/phrases/", parameters, True, self.publicKey, self.privateKey, mashape_callback, True)
		return response

	def sentiment(self, text, mashape_callback=None):
		parameters = {"text" : text}
		mashape_client = HttpClient()
		response = mashape_client.do_call("POST", "http://api.text-processing.com/sentiment/", parameters, True, self.publicKey, self.privateKey, mashape_callback, True)
		return response

	def stem(self, text, language, stemmer, mashape_callback=None):
		parameters = {"text" : text,
		              "language" : language,
		              "stemmer" : stemmer}
		mashape_client = HttpClient()
		response = mashape_client.do_call("POST", "http://api.text-processing.com/stem/", parameters, True, self.publicKey, self.privateKey, mashape_callback, True)
		return response

	def tag(self, text, language, output, mashape_callback=None):
		parameters = {"text" : text,
		              "language" : language,
		              "output" : output}
		mashape_client = HttpClient()
		response = mashape_client.do_call("POST", "http://api.text-processing.com/tag/", parameters, True, self.publicKey, self.privateKey, mashape_callback, True)
		return response
