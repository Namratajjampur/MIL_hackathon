
# coding: utf-8

# In[48]:


import requests
import json
import datetime
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import MobileApplicationClient
client_id = ""
scope = ["activity", "heartrate", "location", "nutrition", "profile", "settings", "sleep", "social", "weight"]


# In[49]:


client = MobileApplicationClient(client_id)
fitbit = OAuth2Session(client_id, client=client, scope=scope)
authorization_url = "https://www.fitbit.com/oauth2/authorize"
auth_url, state = fitbit.authorization_url(authorization_url)
print("Visit this page in your browser: {}".format(auth_url))
callback_url = input("Paste URL you get back here: ")
#print(callback_url)
#callback_url='https://www.fitbit.com/user/5R7NC7#access_token=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkQ1OVAiLCJzdWIiOiI1UjdOQzciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNTQxODIyNjE1LCJpYXQiOjE1NDEyMTkxNjN9.Lf357aDGdaui4GcVYwHXA9cGu4PzyB8jRZZVaSvh6Iw&user_id=5R7NC7&scope=settings+social+nutrition+heartrate+location+sleep+weight+activity+profile&state=2NeikrDGLtEeNhIPLFFZtQsHgHykam&token_type=Bearer&expires_in=603452'
fitbit.token_from_fragment(callback_url)


# In[50]:


token = fitbit.token
print(token)


# In[15]:


'''def mode1():
    heart_rate=fitbit.get('https://api.fitbit.com/1/user/-/activities/heart/date/yesterday/1d.json').json()
    print(heart_rate)
    #hr=heart_rate['activities-heart-intraday']['dataset'][-1]['value']
    #RHR=heart_rate['activities-heart'][0]['value']['restingHeartRate']
    
    hr=59
    if(hr<=RHR+3):
        return True
'''        


# In[16]:


'''ans=mode1()'''


# In[8]:


'''def check_sleep_duration():

    sleep_goal=fitbit.get('https://api.fitbit.com/1/user/-/sleep/goal.json').json()
#print(json.dumps(sleep_goal,indent=2))
    reg_dur=sleep_goal['goal']['minDuration']
#print(reg_dur)
    today_sleep=fitbit.get('https://api.fitbit.com/1.2/user/-/sleep/date/today.json').json()
#print(json.dumps(today_sleep,indent=2))
    today_duration=(today_sleep['sleep'][0]['duration'])/60000
#print(today_duration)
#    if(today_duration<reg_dur):
#        print("you havent slept enough today!")
#        return True
    if(today_duration<500):
        print("you havent slept enough today!")
        return True
'''


# In[35]:


#aa=check_sleep_duration()


# In[51]:


profile= fitbit.get('https://api.fitbit.com/1/user/-/profile.json').json()


# In[34]:


#print(profile)


# In[52]:


def mode1():
    heart_rate=fitbit.get('https://api.fitbit.com/1/user/-/activities/heart/date/2018-11-03/1d.json').json()
    #hr=heart_rate['activities-heart-intraday']['dataset'][-1]['value']
    RHR=heart_rate['activities-heart'][0]['value']['restingHeartRate']
    
    hr=59
    if(hr<=RHR+3):
        return True


# In[53]:


print(mode1())


# In[54]:


def check_sleep_duration():

    sleep_goal=fitbit.get('https://api.fitbit.com/1/user/-/sleep/goal.json').json()
#print(json.dumps(sleep_goal,indent=2))
    reg_dur=sleep_goal['goal']['minDuration']
#print(reg_dur)
    today_sleep=fitbit.get('https://api.fitbit.com/1.2/user/-/sleep/date/2018-11-03.json').json()
#print(json.dumps(today_sleep,indent=2))
    today_duration=(today_sleep['sleep'][0]['duration'])/60000
#print(today_duration)
#    if(today_duration<reg_dur):
#        print("you havent slept enough today!")
#        return True
    if(today_duration<500):
        print("you havent slept enough today!")
        return True



# In[55]:


#print(str(check_sleep_duration()))


# In[45]:


def mode2():
    #now = datetime.datetime.now()
    alarm=fitbit.get('https://api.fitbit.com/1/user/-/devices.json').json()
    today_sleep=fitbit.get('https://api.fitbit.com/1.2/user/-/sleep/date/2018-11-03.json').json()
    #print(today_sleep)
    now= datetime.datetime.strptime('2018-11-03T00:04:30.000','%Y-%m-%dT%H:%M:%S.%f')
    j=''
    #print(today_sleep)
    for i in today_sleep['sleep'][0]['levels']['data']:
        newstr=datetime.datetime.strptime(i['dateTime'],'%Y-%m-%dT%H:%M:%S.%f')
        #print(str(newstr.time())[0:-3])
        b = newstr + datetime.timedelta(0,i['seconds'])
        c=newstr+datetime.timedelta(0,900)
        
        #print(newstr,b,c)
        if(now<=b and now>=newstr):
            state=i['level']
            if(state=='light' or state=='deep' or state=='rem'):
                if(j=='' or j=='wake'):
                    print("WAKE UPPPPPPPPPPPP")
                    alarm1=fitbit.post('https://api.fitbit.com/1/user/-/devices/tracker/'+alarm[0]['id']+'/alarms.json?time='+str(newstr.time())[0:-3]+'-'+str(c.time())[0:-3]+'&enabled=true&recurring=true&weekDays=MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY&snoozeLength=5&snoozeCount=5').json()
                    #print(alarm1)
                    return True
            j=state
            

        


# In[46]:


#print(mode2())
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate(r'C:\Users\Ultrabook\Downloads\milnew-37e66-firebase-adminsdk-y7f2m-66e09c2861.json')
default_app = firebase_admin.initialize_app(cred)
from firebase_admin import db


# In[56]:


from firebase_admin import firestore
#from firebase_admin import db
y=str(check_sleep_duration())
#x=y.decode('utf-8')
#print(x)
db = firestore.client()
db.collection(u'0').document(u'0').set({
   u'TIMESTAMP': firestore.SERVER_TIMESTAMP,
   u'mode1': str(mode1()),
    u'sleep_duration':y,
    u'mode2' :str(mode2())
})

