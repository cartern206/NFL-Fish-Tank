from suntime import Sun, SunTimeException

latitude = 40.544983 
longitude = -112.037132

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
