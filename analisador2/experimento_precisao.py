

from analisador_modificado import Classificador
import nltk

#treino = [(800,1000), (700,1000), (600,1000), (500,1000), (400,1000), (300,1000)]
#teste = (0,250)

treino = [(0,200), (0,300), (0,400), (0,500), (0,600), (0,700), (0,800), (0,900), (0,1000)]
teste = (750,1000)

for a in range(len(treino)):
    cl = Classificador(train1=True, train2=False, train=treino[a], test=teste)
    print nltk.classify.util.accuracy(cl.classifier, cl.testfeats)

