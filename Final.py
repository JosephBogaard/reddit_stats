import requests
import json
import csv
from time import sleep
import random

def getPushshiftData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?size=500&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    sleep(2)
    r = requests.get(url,headers = {'User-agent': 'your bot 0.1'}).text
    data = json.loads(r)
    return data
    
#December 1st 2020
after = 1606780800
#December 31st 2020
before = 1609372800
# https://www.unixtimestamp.com/index.php
#Subreddit: pics
sub = "pics"

###############################
# This method is to find the final ID #
t = before
y = "0"
x = 0
while(x==0):
    gpsd = getPushshiftData(t, before, sub)
    for d in gpsd['data']:
        y = d['id']
    if(y != "0"):
        x = 1
    t-=1000
print(y)
###############################

with open('/home/chuck/Desktop/Queens/two.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    #writer.writerow(['ID','Title','Number of Comments','Score','Upvote Ratio', 'Created UTC', 'Permalink'])
    
    i = 0
    #x = after
    x = 1609372758
    #Crashed at line 3401
    
    #x = utc
    #Crashed at line line
    
    #x = utc
    #Crashed at line line
    while(x < before):
        gpsd = getPushshiftData(x, before, sub)
        for d in gpsd['data']:
            i += 1
            print(f"ID: {d['id']}, Title: {d['title']}")
            print(f"Number of comments: {d['num_comments']}, Score: {d['score']}, Upvote Ratio: {d['upvote_ratio']}, Created UTC: {d['created_utc']}")
            print(f"Permalink: https://www.reddit.com{d['permalink']}")
            writer.writerow([d['id'],d['title'],d['num_comments'],d['score'],d['upvote_ratio'],d['created_utc'],d['permalink']])
            print()
            x = d['created_utc'] + 1
            if(y==d['id']):
                x = before + 1
            print("Post number: ", i, ", UTC: ", x)
    print(x, ' Goodbye')

