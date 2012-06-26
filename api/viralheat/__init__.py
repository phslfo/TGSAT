import urllib2

f = urllib2.urlopen('http://www.viralheat.com/api/sentiment/review.json?text=i%20dont%20like%20this&api_key=ZiCSvzemKrQLiXjPxQTg')
print f.read()
