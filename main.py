

import requests
import json
url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
url2  = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"
response = json.loads(requests.get(url).text)


# In[2]:


#home team name
print(response["events"][0]["competitions"][0]["competitors"][0]["team"]["shortDisplayName"])


# In[3]:


# Score response["events"][0]["competitions"][0]["competitors"][0]["score"]
# team response["events"][0]["competitions"][0]["competitors"][0]["team"]["shortDisplayName"]
# live print response["events"][0]["status"]["type"]["name"]
# pretty print print(json.dumps(teams, indent=4, sort_keys=True))
# shortDisplayName because of the R#*$%!N$


# In[4]:


team0s = json.loads(requests.get(url2).text)

print (team0s)


# In[45]:


teams = {
"Cardinals":["255,0,0",0],
"Falcons":["255,0,0",0],
"Bills":["0,0,255",0],
"Bears":["0,0,255",0],
"Bengals":["255,150,20",0],
"Browns":["255,150,20",0],
"Cowboys":["0,0,255",0],
"Broncos":["0,0,255",0],
"Lions":["0,0,255",0],
"Packers":["0,255,0",0],
"Colts":["0,0,255",0],
"Chiefs":["255,0,0",0],
"Raiders":["255,0,255",0],
"Chargers":["0,0,255",0],
"Rams":["0,0,255",0],
"Dolphins":["0,255,0",0],
"Vikings":["75,0,130",0],
"Patriots":["255,0,0",0],
"Saints":["255,0,255",0],
"Giants":["0,0,255",0],
"Jets":["0,255,0",0],
"Eagles":["0,255,0",0],
"Steelers":["255,0,255",0],
"49ers":["255,0,0",0],
"Titans":["0,0,255",0],
"Jaguars":["0,0,255",0],
"Seahawks":["0,0,255",0],
"Texans":["0,0,255",0],
"Ravens":["75,0,130",0],
"Panthers":["75,0,130",0],
"Buccaneers":["75,0,130",0],   
"Washington":["255,0,0",0]
}

print(teams["Cardinals"])


# In[51]:


for song in response["events"]:   
    #array 
    print (teams[song["competitions"][0]["competitors"][1]["team"]["shortDisplayName"]][1])
    # first team name
    print (song["competitions"][0]["competitors"][1]["team"]["shortDisplayName"])
    #first team score
    print (song["competitions"][0]["competitors"][1]["score"])


# In[50]:


#compare score flash light and update score
 for song in response["events"]:   
     #array 
     if teams[song["competitions"][0]["competitors"][1]["team"]["shortDisplayName"]][1] -1 < int(song["competitions"][0]["competitors"][1]["score"]):
         print ("touchdown")
         teams[song["competitions"][0]["competitors"][1]["team"]["shortDisplayName"]][1] = int(song["competitions"][0]["competitors"][1]["score"])





