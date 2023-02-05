import requests
import time
from playsound import playsound
dist = 294
date = '01-06-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(dist,date)
#https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=294&date=31-05-2021

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
l=[560035,560076,560078,560048,560069,560035]

def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for value in data:
        if((value["available_capacity"]>0) and (value["min_age_limit"]==45) and (value["vaccine"]=="COVAXIN") and (value["pincode"] not in l)):
            counter += 1
            print(value["name"])
            print(value["pincode"])
            print(value["vaccine"])
            print(value["available_capacity"])
            print(value["address"])
            playsound("song.mp3")
            return True
    if(counter == 0):
        print("No Available Slots")
        return False
#COVAXIN

while(findAvailability() != True):
    time.sleep(5)
    findAvailability()
