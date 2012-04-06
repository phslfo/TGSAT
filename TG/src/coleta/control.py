from coleta.models import Tweet, User
import string

def import_from_txt(txt):
    f = open(txt, 'r')

    count = 0
    for line in f:
        count += 1
        data = line.split('%')        
        map(lambda b: string.strip(b), data)
        
        try:
            import datetime
            dt = datetime.datetime.strptime(data[5].strip(), '%Y-%m-%d %H:%M:%S')
            
            if Tweet.get_by_key_name(data[2]):
                continue
            
            user = User.new(data[0], data[1])
            user.save()
            tweet = Tweet.new(data[2], data[3], data[4], dt, user)
            tweet.save()
            
        except:
#            count += count
            import logging
            logging.info(str(count))
#            continue
    
    f.close()
    
    return count
    
def resumo():

    from google.appengine.ext.db import stats
    retorno = ''
    
    stat = stats.KindStat.all()
    for s in stat:
        retorno += str(s.kind_name) + ' - ' + str(s.count) + '\n'
    
    return retorno