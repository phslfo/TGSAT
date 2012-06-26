from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from string import punctuation

ignore_words = ['and', 'the', 'this', 'that']

class Classificador:
    
    def __init__(self, train1=True, train2=True, train3=True, train4=True):
        self.trainfeats = []        
        
        if train1:
            negids = movie_reviews.fileids('neg')
            posids = movie_reviews.fileids('pos')
             
            neg_movies = [(self.word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
            pos_movies = [(self.word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
            
            self.trainfeats = neg_movies + pos_movies
        
        if train2:
            f = open("out.txt", "r")
            
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
        
        if train3:    
            f = open("E:\\Workspace\\WS_TG\\analisador1\\AFINN\\AFINN-111.txt", 'r')
            for l in f:
                data = l.strip().split('\t')
                self.trainfeats.append( (self.word_feats(data[0]), 'neg' if int(data[1]) < 0 else 'pos'))
                
        if train4:
            f = open("E:\\Workspace\\WS_TG\\api\\trainning set.txt", 'r')
            pos = []
            neutral = []
            neg = []
            for line in f:
                if line.startswith("pos"):
                    pos.append(line)
                elif line.startswith("neutral"):
                    neutral.append(line)
                elif line.startswith("neg"):
                    neg.append(line)
                    
            print len(pos), len(neutral), len(neg)
            
            total = pos + neutral[:200] + neg
            
            for line in total:
                data = line.split(' .:. ')
                self.trainfeats.append( (self.word_feats(data[1].split()), data[0]) )
                       
        self.classifier = NaiveBayesClassifier.train(self.trainfeats)
        
        print self.classifier.show_most_informative_features(20)
#        for w in 'In my opinion, the avengers is a spectacular movie, very impressive and a lots of action'.split():
#            print self.analisar2(w)
        
    
    def word_feats(self, words):
        rdata =  dict([(word.strip(punctuation).lower(), True) for word in words])
        return rdata
    
    def analisar(self, text):
        words_gen = [word.strip().strip(punctuation).lower() for word in text.split(' ')
                                                        if len(word) >= 3 and word.lower() not in ignore_words]
                
        feats = self.word_feats(words_gen)
        label = self.classifier.classify(feats) 
        prob = self.classifier.prob_classify(feats)._prob_dict
        
        avg = abs(prob['neg']) + prob['pos']
        if avg > -2.0:
            return {'label' : 'pos', 'prob' : avg}
        elif avg < -3.5:
            return {'label' : 'neg', 'prob' : avg}
        else:
            return {'label' : 'neutral', 'prob' : avg}
    
    def analisar2(self, text):
        words_gen = [word.strip().strip(punctuation).lower() for word in text.split(' ')
                                                        if len(word) >= 3 and word.lower() not in ignore_words]
        
                 
        feats = self.word_feats(words_gen)
        label = self.classifier.classify(feats) 
        prob = self.classifier.prob_classify(feats)._prob_dict
        
        if text.startswith('In my opinion'):
            print prob

        if label == 'pos':
            return {'label' : 'pos', 'prob' : prob['pos']}
        elif label == 'neutral':
            return {'label' : 'neutral', 'prob' : prob['neutral']}
        else:
            return {'label' : 'neg', 'prob' : prob['neg']}