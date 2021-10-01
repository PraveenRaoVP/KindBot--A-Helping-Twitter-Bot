#import gspread if you are using Google spreadsheets to store the words, then use this
import tweepy
import random
import time



#callback_uri='oob' #this is used for opening twitter in browsers

#These 4 arguments are unique to each user and can be obtained from developer twitter API
consumer_key ='' #this is available under API Key
consumer_secret ='' #API key secret
token ='' #Access Token
token_secret ='' #Access token secret

#OAuthHandler authenticates the above details.
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#establishes connection
auth.set_access_token(token,token_secret)
#API variable for connection to twitter Dev API
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#api.update_status("Test") simply for testing purpose. Go to the Twitter 
#@KindBot2 for the output

#this file contains the people who tagged the bot
FILE_NAME='tagged_users.txt'
#Empty file just in case for the kindness shower
file_name=""

#get the user tag who tagged the bot
def get_tagged_users(file_name):
     f=open(file_name ,'r')
     tag_user=f.read().strip()
     f.close()
     return tag_user

def put_tagged_user(tag_user, file_name):
     f=open(file_name ,'w')
     f.write(str(tag_user))
     f.close()
     return 


def take_kind_words(file_name):
     f=open(file_name ,'r')
     kind=f.read().split('\n')
     return kind

#choose the kind statement
def pick_statement():
     kind=take_kind_words('kindness.txt')
     kind_words=random.choice(kind)
     return kind_words

#tweet the kind statement to user
def tweet_to_user():
     kindness_words=pick_statement()
     kindness_words=""
     kindness_words=pick_statement()
     tagger_user=get_tagged_users(FILE_NAME)
     put_tagged_user(tagger_user,FILE_NAME)
     mention=api.mentions_timeline()
     for mentions in reversed(mention):
          tagger_user=mentions.id
          put_tagged_user(tagger_user,FILE_NAME)
          api.update_status('@'+ mentions.user.screen_name +' '+ kindness_words, in_reply_to_status_id=mentions.id)
          print("Tweeted @"+mentions.user.screen_name+" "+kindness_words+"\n")
          time.sleep(10)

print("Bot started")
while(True):
     print("Welcome to Kindbot!")
     tweet_to_user()
     break
