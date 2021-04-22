pip install pytz
pip install astral
import pytz
from datetime import datetime
from astral.sun import sun
from astral import LocationInfo
city = LocationInfo("Salt Lake City")
now = datetime.now() 
s = sun(city.observer, date=now, tzinfo=city.timezone)


from astral import LocationInfo
city = LocationInfo("Salt Lake City")


if now.replace(tzinfo=pytz.UTC) > s["sunrise"].replace(tzinfo=pytz.UTC):
    print("working")
else: print("broken")
    
