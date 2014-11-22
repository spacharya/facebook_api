from gettext import find

__author__ = 'Suraj'

import pprint
import requests
import random
import json

'''
    This code helps in liking and commenting on posts on Facebook on your birthday
    '''

url_base = "https://graph.facebook.com/v2.1/"
url_req = "me/feed"

# Accepts the Auth Token. Will need to generate it via Graph API Explorer.
auth_val = input("Enter the Authentication Token")
timeval = input('Enter time from till when in the past.Either in the format of YYYY-MM-DD or YYYY-MM-DD HH:MM')
if timeval.count(":") > 0:
    timeval = timeval.replace(" ","T")
    timeval = timeval+":00+0000"
else:
    timeval = timeval + "T00:00:00+0000"
print(timeval)
authtoken = '?access_token=' + auth_val
fb = open("facebook.txt", "w")
url_send = url_base + url_req + authtoken
# Used to hold the ID of the posts on your wall. Will be useful when replying to it.
id = []
ctime = []
breaker = False
for j in range (0 , 100):
    r = requests.get(url_send)
    jsonobj = json.loads(r.text)
    data = jsonobj.get("data")
    for i in data:
        idv = i.get('id')
        time = i.get('created_time')
        if time < timeval:
            breaker = True
            break
        elif idv not in id:
            id.append(idv)
            ctime.append(time)
    url_send = jsonobj.get('paging').get('next')
    if breaker:
        break
'''
    Reading the file to get a better message list
    will need to save the messages as message.txt
    '''
msg = []
msgfile = open("message.txt" , "r")
for line in msgfile:
    msg.append(line)
for idv in id:
    url_like = url_base + idv + "/likes" + authtoken
    print(url_like)
    r = requests.post(url_like)
    url_comment = url_base + idv + "/comments" + authtoken
    h = {'message' : msg[random.randint(0,len(msg)-1)]}
    r = requests.post(url_comment , data = h)
    # print(r.text)






