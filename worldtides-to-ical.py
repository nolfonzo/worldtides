from datetime import timedelta
import pathlib 
from pathlib import Path
from datetime import datetime, timedelta
import json
import ics
from ics import Calendar, Event, DisplayAlarm, AudioAlarm
import urllib.request
c = Calendar()
tidedict = json.loads(urllib.request.urlopen('https://www.worldtides.info/api/v2?heights&extremes&date=2021-11-09&lat=-33.53863&lon=151.24155&days=365&datum=LAT&key=926cd23d-594e-40bd-b86b-06f9fe83ee2f').read())
c.name=tidedict["station"]
for key in tidedict["extremes"]:
    e = Event()
    e.name=key["type"] + ": " + str(key["height"])
    e.begin=key["date"]
    e.end=key["date"]
    a=DisplayAlarm()
    a.trigger=timedelta(seconds=1)
    a.display_text=key["type"] + " tide alert!"
    e.alarms=[a]
    c.events.add(e)
#   print(c)
with open(pathlib.Path.home() / "src" / "worldtides" / "dangar.ics", 'w') as my_file:
    my_file.writelines(c)