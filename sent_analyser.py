from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
def percentage(part,whole):
    return 100* float(part)/float(whole)

ckey="5YRbACZU0lHWSZDSUhSmCGEJS"
csecret="07eZevetVdcXN7Y2CwSKBaMMIJBUkBHOwiG7Rq78hIxRA5m4tX"
accesstoken="1169554705376141312-kaWm2PBXhl3I4m4HmfzwRGU3I4r8rb"
accesstokensecret="jF2xZPe2P4TSGFfCp1IkwS06eLTdPg7cYBQ1h7a79h5hU"

auth=tweepy.OAuthHandler(consumer_key=ckey,consumer_secret=csecret)
auth.set_access_token(accesstoken,accesstokensecret)
api=tweepy.API(auth)

searchterm=input("Enter Keyword/hastag to search about:")
nosearchterms=int(input("Enter how many tweets to analyse:"))

tweets=tweepy.Cursor(api.search,q=searchterm).items(nosearchterms)



positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity==0):
        neutral +=1
    elif(analysis.sentiment.polarity<0.00):
        negative +=1
    elif(analysis.sentiment.polarity>0.00):
        positive +=1

positive=percentage(positive,nosearchterms)
negative=percentage(negative,nosearchterms)
neutral=percentage(neutral,nosearchterms)

positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')

print("How people are reacting on" + searchterm + "by analysing" + str(nosearchterms) +"tweets")
if(polarity==0):
    print("Neutral")
elif(polarity<0):
    print("Negative")
elif(polarity>0):
    print("Positive")

labels= ['Positive['+str(positive)+ '%]',  'Negative[' + str(negative) + '%]','Neutral[' + str(neutral) + '%]']

sizes=[positive,negative,neutral]
colors=['yellow','red','green']
patches, texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title("How people are reacting to " + '#' + searchterm + " by analysing " + str(nosearchterms) + " tweets")
plt.axis('equal')
plt.tight_layout()
plt.show()