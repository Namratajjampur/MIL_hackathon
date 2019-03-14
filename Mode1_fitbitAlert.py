
# coding: utf-8

# In[136]:


import requests
import json
import datetime
from firebase_admin import db
import webbrowser
# Get a database reference to our blog.
ref = db.reference('users/ada')
users_ref = ref.child('users')


# In[137]:


from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import MobileApplicationClient


# In[138]:


client_id = ""


# In[139]:


scope = ["activity", "heartrate", "location", "nutrition", "profile", "settings", "sleep", "social", "weight"]


# In[140]:


client = MobileApplicationClient(client_id)
fitbit = OAuth2Session(client_id, client=client, scope=scope)
authorization_url = "https://www.fitbit.com/oauth2/authorize"
auth_url, state = fitbit.authorization_url(authorization_url)
print("Visit this page in your browser: {}".format(auth_url))
callback_url = input("Paste URL you get back here: ")
#print(callback_url)
#callback_url='https://www.fitbit.com/user/5R7NC7#access_token=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkQ1OVAiLCJzdWIiOiI1UjdOQzciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNTQxODIyNjE1LCJpYXQiOjE1NDEyMTkxNjN9.Lf357aDGdaui4GcVYwHXA9cGu4PzyB8jRZZVaSvh6Iw&user_id=5R7NC7&scope=settings+social+nutrition+heartrate+location+sleep+weight+activity+profile&state=2NeikrDGLtEeNhIPLFFZtQsHgHykam&token_type=Bearer&expires_in=603452'
fitbit.token_from_fragment(callback_url)


# In[141]:


token = fitbit.token
print(token)


# In[142]:


profile= fitbit.get('https://api.fitbit.com/1/user/-/profile.json').json()
#print(json.dumps(profile,indent=2))


# In[143]:


#heart_rate=fitbit.get('https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json').json()
#print(json.dumps(heart_rate,indent=2))


# In[144]:


#print(heart_rate['activities-heart'][0]['value']['restingHeartRate'])
#RHR=heart_rate['activities-heart'][0]['value']['restingHeartRate']
#print(RHR)


# In[145]:


#last_HR =heart_rate['activities-heart-intraday']['dataset'][-1]['value']
'''last_HR=59
#
if(last_HR<=RHR+3):
    
    print("heart rate has come close to your rest hear reat.. tired?")
    check_sleep_duration()
    
 '''   


# In[146]:


def mode1():
    heart_rate=fitbit.get('https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json').json()
    #hr=heart_rate['activities-heart-intraday']['dataset'][-1]['value']
    RHR=heart_rate['activities-heart'][0]['value']['restingHeartRate']
    
    hr=59
    if(hr<=RHR+3):
        return True
        


# In[147]:


def check_sleep_duration():

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



# In[148]:


#sleep_generate=fitbit.post('https://api.fitbit.com/1.2/user/-/sleep.json?date=2018-11-03&startTime=02:32&duration=7200000').json()
#print(sleep_generate)


# In[149]:


#print(json.dumps(today_sleep,indent=2))


# In[150]:


#print(json.dumps(today_sleep['sleep'][0]['levels']['data'],indent=2))
    


# In[151]:


#now = datetime.datetime.now()
#now= datetime.datetime.strptime('2018-11-03T00:04:30.000','%Y-%m-%dT%H:%M:%S.%f')


# In[152]:


def mode2():
    #now = datetime.datetime.now()
    alarm=fitbit.get('https://api.fitbit.com/1/user/-/devices.json').json()
    today_sleep=fitbit.get('https://api.fitbit.com/1.2/user/-/sleep/date/today.json').json()
    now= datetime.datetime.strptime('2018-11-03T00:04:30.000','%Y-%m-%dT%H:%M:%S.%f')
    j=''
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
            

        


# In[153]:


mode1= mode1()
print(mode1)


# In[154]:


check_sleep_duration=check_sleep_duration()
print(check_sleep_duration)


# In[107]:


mode3=mode2()
s=str(mode3)
u = unicode(s, "utf-8")


# In[70]:


#alarm=fitbit.get('https://api.fitbit.com/1/user/-/devices.json').json()
#print(alarm)
#print(type(alarm[0]['id']))


# In[69]:


#alarm1=fitbit.post('https://api.fitbit.com/1/user/-/devices/tracker/'+alarm[0]['id']+'/alarms.json?time=08:45-09:00&enabled=true&recurring=true&weekDays=MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY&snoozeLength=5&snoozeCount=5').json()


# In[68]:


#print(alarm1)


# In[103]:


import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate(r'C:\Users\Ultrabook\Downloads\milnew-37e66-firebase-adminsdk-y7f2m-66e09c2861.json')
default_app = firebase_admin.initialize_app(cred)
from firebase_admin import db


# In[105]:


from firebase_admin import firestore
db = firestore.client()
db.collection(u'1').document(u'1').set({
   u'TIMESTAMP': firestore.SERVER_TIMESTAMP,
   u'mode1': u'',
})

