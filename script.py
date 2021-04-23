
import time
import board
import neopixel
import requests
import json
from datetime import datetime
import pytz
from astral.sun import sun
from astral import LocationInfo
url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"


 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 7
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=255, auto_write=False, pixel_order=ORDER
)
teams = {
"Cardinals":[(255,0,0),(150,150,150),0],
"Falcons":[(255,0,0),(10,10,10),0],
"Bills":[(0,51,141),(198,12,48),0],
"Bears":[(0,0,255),(255,69,0),0],
"Bengals":[(255,69,0),(255,255,255),0],
"Browns":[(251,79,20),(0,0,0),0],
"Cowboys":[(0,0,255),(255,255,255),0],
"Broncos":[(0,0,255),(255,69,0),37],
"Lions":[(4,10,180),(255,255,255),0],
"Packers":[(0,255,0),(255, 255, 0),0],
"Colts":[(0,0,255),(255,255,255),0],
"Chiefs":[(255,0,0),(255,255,0),0],
"Raiders":[(255,255,255),(0,0,0),0],
"Chargers":[(0,0,255),(255,255,0),0],
"Rams":[(0,53,148),(255,255,0),0],
"Dolphins":[(0,255,255),(255,69,0),0],
"Vikings":[(75,0,130),(255, 255, 0),0],
"Patriots":[(255,0,0),(0,0,255),0],
"Saints":[(204,175,141),(255,255,255),0],
"Giants":[(25,46,108),(255,51,0),0],
"Jets":[(0,255,0),(255,255,255),28],
"Eagles":[(0,255,0),(255,255,255),0],
"Steelers":[(255,194,14),(0,0,0),0],
"49ers":[(201,36,63),(200,170,118),0],
"Titans":[(64,149,209),(0,41,91),0],
"Jaguars":[(216,163,40),(19,102,119),0],
"Seahawks":[(0,42,92),(51,255,0),-5],
"Texans":[(0,20,63),(201,36,63),0],
"Ravens":[(75,0,130),(0,0,0),0],
"Panthers":[(0,133,202),(191,192,191),0],
"Buccaneers":[(212,9,9),(178,185,191),0],   
"Washington":[(124,20,21),(255,194,15),0]
}
city = LocationInfo("Salt Lake City")            
while True:
   # print (datetime.now())
    try:
        response = json.loads(requests.get(url).text)
    except:
        print("error")
        print (datetime.now())
    city = LocationInfo("Salt Lake City")
    now = datetime.now() 
    s = sun(city.observer, date=now, tzinfo=city.timezone)
    if s["sunset"].replace(tzinfo=pytz.UTC)>now.replace(tzinfo=pytz.UTC) > s["sunrise"].replace(tzinfo=pytz.UTC):
        tank = pixels.fill((255, 255, 255))
    else: tank = pixels.fill((5,5,(255/(now.second+1)))
    tank
    pixels.show()
    y=0
    for song in response["events"]:
        
    for song in response["events"]:   
     #array 
        x = 0

        while x < 2:
            if teams[song["competitions"][0]["competitors"][x]["team"]["shortDisplayName"]][2] +1  < int(song["competitions"][0]["competitors"][x]["score"]):
                print (song["competitions"][0]["competitors"][x]["team"]["shortDisplayName"])
                print (song["competitions"][0]["competitors"][x]["score"])
                i=0
                while i < 6:
                    pixels.fill((0, 0, 0))
                    pixels.show()
                    pixels.fill(teams[song["competitions"][0]["competitors"][x]["team"]["shortDisplayName"]][0])
                    pixels.show()
                    time.sleep(1)
                    pixels.fill(teams[song["competitions"][0]["competitors"][x]["team"]["shortDisplayName"]][1])
                    pixels.show()
                    time.sleep(1)
                    i += 1
                tank
                pixels.show()
                teams[song["competitions"][0]["competitors"][x]["team"]["shortDisplayName"]][2] = int(song["competitions"][0]["competitors"][x]["score"])
            x+= 1
    #time.sleep(5)    

