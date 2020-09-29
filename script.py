
import time
import board
import neopixel
import requests
import json
url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
response = json.loads(requests.get(url).text)

 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 7
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
teams = {
"Cardinals":[(255,0,0),0],
"Falcons":[(255,0,0),0],
"Bills":[(0,0,255),0],
"Bears":[(0,0,255),0],
"Bengals":[(255,150,20),0],
"Browns":[(255,150,20),0],
"Cowboys":[(0,0,255),0],
"Broncos":[(0,0,255),0],
"Lions":[(0,0,255),0],
"Packers":[(0,255,0),0],
"Colts":[(0,0,255),0],
"Chiefs":[(255,0,0),0],
"Raiders":[(255,0,255),0],
"Chargers":[(0,255,0),0],
"Rams":[(0,255,0),0],
"Dolphins":[(0,255,0),0],
"Vikings":[(75,0,130),0],
"Patriots":[(255,0,0),0],
"Saints":[(0,255,0),0],
"Giants":[(0,0,255),0],
"Jets":[(0,255,0),0],
"Eagles":[(0,255,0),0],
"Steelers":[(255,0,255),0],
"49ers":[(255,0,0),0],
"Titans":[(0,0,255),0],
"Jaguars":[(0,0,255),0],
"Seahawks":[(0,0,255),0],
"Texans":[(0,0,255),0],
"Ravens":[(75,0,130),0],
"Panthers":[(0,0,255),0],
"Buccaneers":[(255,0,0),0],   
"Washington":[(255,0,0),0]
}
while True:
    response = json.loads(requests.get(url).text)
    for song in response["events"]:   
     #array 
        if teams[song["competitions"][0]["competitors"][1]["team"]["shortDisplayName"]][1] -1 < int(song["competitions"][0]["competitors"][1]["score"]):
            i=0
            while i < 3:
                pixels.fill((0, 0, 0))
                pixels.show()
                pixels.fill(teams[song["competitions"][0]["competitors"][1]["team"]["shortDisplayName"]][0])
                pixels.show()
                time.sleep(.7)
                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(.7)
                i += 1
            teams[song["competitions"][0]["competitors"][1]["team"]["shortDisplayName"]][1] = int(song["competitions"][0]["competitors"][1]["score"])

   
