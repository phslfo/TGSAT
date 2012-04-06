# Code inspired and developed from: 
# http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
# Original Code: https://gist.github.com/1410094

from __future__ import division
import nltk
from string import punctuation

class Classificador:
    
    def __init__(self):
        # Load data set
        moviedataset = []
        for group in ['neg', 'pos']:
            fids = nltk.corpus.movie_reviews.fileids(group)
            for fid in fids:
                item = (self.features(nltk.corpus.movie_reviews.words(fileids=[fid])), group)  
                moviedataset.append(item)
                
        # Train classifier
        self.classifier = nltk.classify.NaiveBayesClassifier.train(moviedataset)
#        accuracy = nltk.classify.util.accuracy(self.classifier, moviedataset)
#        print("Training set accuracy: %.3f" % (accuracy,))
    
    def features(self, wordlist):
        return dict([ (word, True) for word in wordlist ])
    
    def analisar(self, text):
        words_gen = [word.strip().strip(punctuation).lower() for word in text.split(' ')
                                                        if len(word) >= 3]
        
        feats = self.features(words_gen)
        label = self.classifier.classify(feats) 
        prob = self.classifier.prob_classify(feats)
        
        return label





