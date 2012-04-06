from google.appengine.ext import db   


class User(db.Model):
    name            = db.StringProperty()
    screen_name     = db.StringProperty()
    
    @staticmethod
    def new(name, screen_name):
        return User(key_name=screen_name, name=name, screen_name=screen_name)  
    

class Tweet(db.Model):    
    text            = db.StringProperty()
    author_location = db.StringProperty()
    tweet_location  = db.StringProperty()
    date            = db.DateTimeProperty()
    user            = db.ReferenceProperty(reference_class=User)
    
    @staticmethod
    def new(text, author_location, tweet_location, date, user):
        return Tweet(key_name=text , text=text, author_location=author_location, 
                     tweet_location=tweet_location, date=date, user=user)
        