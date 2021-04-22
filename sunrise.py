
## if song["competitions"][0]["status"]['clock'] > 0:
pip install pytz
pip install astral
import pytz
from datetime import datetime
from astral.sun import sun
from astral import LocationInfo
city = LocationInfo("Salt Lake City")
now = datetime.now() 
s = sun(city.observer, date=now, tzinfo=city.timezone)
if s["sunset"].replace(tzinfo=pytz.UTC)>now.replace(tzinfo=pytz.UTC) > s["sunrise"].replace(tzinfo=pytz.UTC):
    print("cool")
else: print("broken")
    
