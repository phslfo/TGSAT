from nltk.corpus import movie_reviews
import analisador

def word_feats(words):
    rdata = ""
    for word in words:
        rdata += word
        
    return rdata

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

neg_movies = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
pos_movies = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

testfeats = neg_movies[750:1000] + pos_movies[750:1000]
acertos = 0
for a in testfeats:
    if analisador.sentiment(a[0])['label'] == a[1]:
        acertos += 1

print 'accuracy:', acertos/float(len(testfeats))
