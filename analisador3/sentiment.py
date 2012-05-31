"""
@package sentiment
Twitter sentiment analysis.

This code performs sentiment analysis on Tweets.

A custom feature extractor looks for key words and emoticons.  These are fed in
to a naive Bayes classifier to assign a label of 'positive', 'negative', or
'neutral'.  Optionally, a principle components transform (PCT) is used to lessen
the influence of covariant features.

"""
import csv, random
import nltk
import tweet_features, tweet_pca
from string import punctuation

# read all tweets and labels


class Classifier():
    
    def __init__(self):
        
        fp = open( 'sentiment.csv', 'rb' )
        reader = csv.reader( fp, delimiter=',', quotechar='"', escapechar='\\' )
        tweets = []
        
        for row in reader:
            try:
                data = row[0].split(',')
                if data[1].replace('"', '') != '' and data[1].replace('"', '') != 'Sentiment':
                    tweets.append( [data[4], data[1].replace('"', '')] );
            except:
                continue
        
        
        # treat neutral and irrelevant the same
        for t in tweets:
            if t[1] == '"irrelevant"':
                t[1] = 'neutral'
        
        v_train = [(tweet_features.make_tweet_dict(t),s) for (t,s) in tweets]
        self.classifier = nltk.NaiveBayesClassifier.train(v_train);
        
    def word_feats(self, words):
        return dict([(word, True) for word in words])
    
    def analisar(self, text):
#        words_gen = [word.strip().strip(punctuation).lower() for word in text.split(' ')
#                                                        if len(word) >= 3]
                
        feats = tweet_features.make_tweet_dict(text)
        label = self.classifier.classify(feats) 
#        prob = self.classifier.prob_classify(feats)._prob_dict
        
        if label == 'negative':
            return {'label' : 'neg', 'prob' : 0}
        elif label == 'positive':
            return {'label' : 'pos', 'prob' : 0}
        elif label == 'neutral':
            return {'label' : 'neutral', 'prob' : 0}
        else:
            return {'label' : 'error', 'prob' : 0}

#        avg = abs(prob['negative']) + prob['positive"']
#        if avg > 0:
#            return {'label' : 'pos', 'prob' : avg}
#        elif abs(avg) > 2.5:
#            return {'label' : 'neg', 'prob' : avg}
#        else:
#            return {'label' : 'neutral', 'prob' : avg}

# dump tweets which our feature selector found nothing
#for i in range(0,len(tweets)):
#    if tweet_features.is_zero_dict( fvecs[i][0] ):
#        print tweets[i][1] + ': ' + tweets[i][0]


# apply PCA reduction
#(v_train, v_test) = \
#        tweet_pca.tweet_pca_reduce( v_train, v_test, output_dim=1.0 )


# train classifier
#classifier = nltk.NaiveBayesClassifier.train(v_train);
#classifier = nltk.classify.maxent.train_maxent_classifier_with_gis(v_train);


# classify and dump results for interpretation
#print '\nAccuracy %f\n' % nltk.classify.accuracy(classifier, v_test)
#print classifier.show_most_informative_features(200)


# build confusion matrix over test set
#test_truth   = [s for (t,s) in v_test]
#test_predict = [classifier.classify(t) for (t,s) in v_test]
#
#print 'Confusion Matrix'
#print nltk.ConfusionMatrix( test_truth, test_predict )
