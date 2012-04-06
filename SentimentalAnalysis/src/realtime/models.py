
from django.db.models.base import Model

class User(Model):
#    user_id         = db.StringProperty()
#    screen_name     = db.StringProperty()
#    image           = db.StringProperty()    
    
    @staticmethod
    def new(user_id, screen_name, image):
        return User(user_id=user_id, screen_name=screen_name, image=image)  

class Tweet(Model):    
#    tweet_id        = db.StringProperty()
#    text            = db.StringProperty()
#    date            = db.DateTimeProperty()
#    user            = db.ReferenceProperty(reference_class=User)
    
    @staticmethod
    def new(tweet_id, text, date, user):
        return Tweet(tweet_id=tweet_id, text=text, date=date, user=user)
    
        
