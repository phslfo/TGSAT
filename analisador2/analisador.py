import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from string import punctuation

class Classificador:
    
    def __init__(self):
        negids = movie_reviews.fileids('neg')
        posids = movie_reviews.fileids('pos')
         
        negfeats = [(self.word_feats(movie_reviews.words(fileids=[f])), 'negative') for f in negids]
        posfeats = [(self.word_feats(movie_reviews.words(fileids=[f])), 'positive') for f in posids]
        trainfeats = negfeats + posfeats
        
        self.classifier = NaiveBayesClassifier.train(trainfeats)
    
    def word_feats(self, words):
        return dict([(word, True) for word in words])
    
    def analisar(self, text):
        words_gen = [word.strip().strip(punctuation).lower() for word in text.split(' ')
                                                        if len(word) >= 3]
        
        feats = self.word_feats(words_gen)
        label = self.classifier.classify(feats) 
        prob = self.classifier.prob_classify(feats)
        
        return label

 
#negcutoff = len(negfeats)*3/4
#poscutoff = len(posfeats)*3/4


#trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
#testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
#print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 

#print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
#classifier.show_most_informative_features()

#print classifier.classify(word_feats(["horrible"]))