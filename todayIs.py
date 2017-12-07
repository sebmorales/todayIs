import vimeo
import subprocess
from vidpy import Clip, Composition
import json
import requests
import time;  # This is required to include time module.
import datetime;


week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
year=datetime.date.today().strftime("%Y")
month=datetime.date.today().strftime("%B")
weekday=datetime.date.today().strftime("%w")
weekday=week[int(weekday)]
day=datetime.date.today().strftime("%d")
today=('Today is '+weekday+' '+day+' '+month+' '+year)

clip_today=Clip('videos/todayis.mov').set_offset(0)
clip_weekDay=Clip('videos/'+weekday+".mov").set_offset(2)
composition=Composition([clip_today,clip_weekDay])
composition.save('today.mp4')


with open("creds.json") as infile:
    creds=json.load(infile)

ACCESS_TOKEN=creds["ACCESS_TOKEN"]
CLIENT_SECRET=creds["CLIENT_SECRET"]
CLIENT_ID=creds["CLIENT_ID"]
v=vimeo.VimeoClient(
    token=ACCESS_TOKEN,
    key=CLIENT_ID,
    secret=CLIENT_SECRET
)
# TO UPLOAD:
#video_uri = v.upload('today.mp4')

# TO REPLACE:
payload = {'title': today}
URL='https://api.vimeo.com/videos/246202348'
v.replace(
    video_uri=URL,
    filename='today.mp4',
    name=today,
    description='Video calendar informing every day\'s date'
    )
 # print payload['title']
v.patch(URL, data={'name': today, 'description': 'Calendar'})
