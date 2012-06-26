
f_test = open('test set.txt', 'r')
f_trainning = open('trainning set.txt', 'r')

all_trainning = [line.split(' .:. ')[1].strip() for line in f_trainning.readlines()]
print 'Tamanho treinamento', len(all_trainning)

all_test = [line.split(' .:. ')[1].strip() for line in f_test.readlines()]
print 'Tamanho teste', len(all_test)

for line in all_test:
    if line in all_trainning:
        print line.strip()