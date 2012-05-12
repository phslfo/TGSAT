from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from string import punctuation
import nltk

ignore_words = ['rick']

class Classificador:
    
    def __init__(self, train1=True, train2=True, test=(0,0), train=(0,0)):
        
        self.trainfeats = []        
        
        if train1 or test != (0,0):
            negids = movie_reviews.fileids('neg')
            posids = movie_reviews.fileids('pos')
             
            neg_movies = [(self.word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
            pos_movies = [(self.word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
            
            self.testfeats = neg_movies[test[0]:test[1]] + pos_movies[test[0]:test[1]]
            
        if train1:
            self.trainfeats = neg_movies[train[0]:train[1]] + pos_movies[train[0]:train[1]]
        
        if train2:
            f = open("training.txt", "r")
            
            negfeats = []
            posfeats = []
            for line in f:
                status = line[0]
                texto = line[2:]
    
                if status == '0':
                    negfeats.append((self.word_feats(texto.split(" ")), 'neg'))
                elif status == '1':
                    posfeats.append((self.word_feats(texto.split(" ")), 'pos'))               
        
            self.trainfeats += negfeats + posfeats
                       
        self.classifier = NaiveBayesClassifier.train(self.trainfeats)
    
    def word_feats(self, words):
        return dict([(word, True) for word in words])
    
    def analisar(self, text):
        words_gen = [word.strip().strip(punctuation).lower() for word in text.split(' ')
                                                        if len(word) >= 3 and word.lower() not in ignore_words]
                
        feats = self.word_feats(words_gen)
        label = self.classifier.classify(feats) 
        prob = self.classifier.prob_classify(feats)._prob_dict
            
        avg = abs(prob['neg']) + prob['pos']
        if avg > 0:
            return {'label' : 'pos', 'prob' : avg}
        elif abs(avg) > 2.5:
            return {'label' : 'neg', 'prob' : avg}
        else:
            return {'label' : 'neutral', 'prob' : avg}
        

 
#negcutoff = len(negfeats)*3/4
#poscutoff = len(posfeats)*3/4


#trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
#testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
#print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 

#print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
#classifier.show_most_informative_features()

#print classifier.classify(word_feats(["horrible"]))