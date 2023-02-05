#https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=294&date=31-05-2021
#l=[560064,560010,560054,560003,560063,560015]
#from selenium import webdriver
#(value["pincode"] not in [560064])
import requests
import webbrowser
import time
import datetime
from playsound import playsound
dist = 294
date = '05-02-2023'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(dist,date)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def booking():
    '''
    driver = webdriver.Chrome()
    driver.get('https://selfregistration.cowin.gov.in')
    mobno = driver.find_element_by_id('mat-input-0')
    mobno.send_keys('9916496981')
    get_otp = driver.find_element_by_type('button')
    get_otp.click()

if((value["available_capacity"]>0) and (value["min_age_limit"]==45) and (value["vaccine"]=="COVAXIN") and (value["pincode"]  in [560076,560010,560003,560063,560015,560068])):
    
    '''
    webbrowser.open("https://selfregistration.cowin.gov.in", new=1)
    playsound("song.mp3")


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for value in data:
        print(value)
        if((value["available_capacity_dose2"]>0) and(value["vaccine"]=="COVAXIN") and (value["pincode"]  in [560076,560010,560003,560063,560015,560068])):
       # if((value["pincode"]  in [560076,560010,560003,560063,560015,560068])):
            counter += 1
            print(value["name"])
            print(value["pincode"])
            print(value["vaccine"])
            print(value["available_capacity"])
            print(value["address"])
            booking()
            return True
    if counter == 0:
        print("No Available Slots", end='')
        print(":-", end='')
        now = datetime.datetime.now()
        time = now.strftime("%H:%M:%S")
        print(time)
        return False
#COVAXIN

while(findAvailability() != True):
    time.sleep(5)
    findAvailability()
