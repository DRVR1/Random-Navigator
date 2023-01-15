from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Union
import time
from timeit import default_timer as timer
import random
import fake_useragent
import datetime
import os

'''
author: ianvid
'''
#config (random intervals (from, to) in the selected time unit)
timeUnit = 1 # 1-seconds 2-hours
staytimeT = (15,15) #time it stays in a website in seconds 
totaltimeT = (35,35) #time the browser is open before close
breaktimeT = (10,10) #how much to wait before re-open the browser
startups = 3 #times the browser will close and re-open again to simulate a break from browsing (if 0, it never closes)
wbrowser = 3 # 1-chrome 2-firefox 3-edge
fontcolor = '7'  #console font color (windows only)
'''
windows OS options:
    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
'''
if os.name == 'nt': #if OS is windows, change console font color
    os.system('color ' + fontcolor)

#other config
sitesfile = 'randomsites.txt' #list of websites (you can use generator.py to generate a list of random links inside a webpage or wepages you choose)


class Controller:
    def __init__(self, staytimeT:tuple, totaltimeT:tuple, breaktimeT:tuple, startups:int) -> None:
        '''
        staytimeT:  random interval of time it stays in a website in seconds (from, to) 
        totaltimeT: time the browser is open before close
        breaktimeT: how much to wait before re-open the browser

        usage: Controller(params).randomize()
        '''
        self.staytimeT = staytimeT
        self.totaltimeT = totaltimeT
        self.breaktimeT = breaktimeT

        self.staytime = 0
        self.totaltime = 0
        self.breaktime = 0
        self.startups = startups

        self.startTime = timer()

    def randomize(self):
        print("randomizing values...")
        self.staytime = random.uniform(self.staytimeT[0],self.staytimeT[1])
        self.totaltime = random.uniform(self.totaltimeT[0],self.totaltimeT[1])
        self.breaktime = random.uniform(self.breaktimeT[0],self.breaktimeT[1])
        
        if(timeUnit == 2):
            self.staytime = self.staytime*3600
            self.totaltime = self.totaltime*3600
            self.breaktime = self.breaktime*3600
            self.timeUnitString = 'seconds'
        if(timeUnit == 1):
            self.timeUnitString = 'seconds'


        print("staying in website for: " + str(self.staytime) + ' '+self.timeUnitString)
        print("open browser max time: "+ str(self.totaltime) + ' '+self.timeUnitString)
        print("resting time: "+ str(self.breaktime) + ' '+self.timeUnitString)

    def getOptions(self)->int:
        '''
        staytime, totaltime, breaktime
        '''
        return self.staytime, self.totaltime,self.breaktime

    def resetTimer(self):
        print("reseting timer...")
        self.startTime = timer()


class Browser:
    def __init__(self,setRandomAgent = False) -> None:
        #data
        self.searchedsites = 0
        self.currentstartup = 0

        self.options = Options()
        arguments = ['disable-infobars'] #remove "chrome is being controlled by automated test software"
        self.options.add_experimental_option("excludeSwitches", ['enable-automation']);  #remove "chrome is being controlled by automated test software"
        for arg in arguments:
            self.options.add_argument(arg)
        if(setRandomAgent):
            ua = fake_useragent.UserAgent()
            userAgent = ua.random
            self.options.add_argument(f'user-agent={userAgent}') #setting a random useragent

    def open(self, which:int) -> Union[webdriver.Chrome,webdriver.Firefox,webdriver.Edge]:
        '''
        1-chrome
        2-firefox
        3-edge
        '''
        print("opening browser...")
        if(which==1):
            self.driver = webdriver.Chrome(options=self.options) #only set the options for chrome
        if(which==2):
            self.driver = webdriver.Firefox()
        if(which==3):
            self.driver = webdriver.Edge()

        self.currentstartup += 1
        return self.driver

    def search(self,sites:list,controller:Controller):
        currentTime = timer()
        elapsedTime = currentTime - controller.startTime
        print("current browsing time: " + str(elapsedTime) + ' '+controller.timeUnitString)
        index = random.randint(0,len(sites)-1)
        site = sites[index]
        self.searchedsites += 1
        if(controller.startups != 0):
            print("startup: " + str(self.currentstartup) + '/' + str(controller.startups))
            if(elapsedTime > controller.totaltime):
                return True #breaks the loop
        print('total visited sites: ' + str(self.searchedsites))
        print("loading: "+site)
        self.driver.get(site)
        print(str(datetime.datetime.now()) + " - loaded, staying: " +str(controller.staytime) + ' '+controller.timeUnitString)
        time.sleep(controller.staytime)

    def close(self):
        print("closing browser... this may take some seconds depending on the browser")
        self.driver.close()

#get data from the file
sites = []
f = open(sitesfile,'r')
lines = f.readlines()
for line in lines:
    print("readed line: " + line)
    sites.append(line)
f.close()


controller = Controller(staytimeT,totaltimeT,breaktimeT,startups)
controller.randomize()
br = Browser(controller)
br.open(wbrowser)

print('starting')
if(startups == 0):
    while(True):
        br.search(sites,controller)
        controller.randomize()
else:
    while(True):
        print("===========================================")
        controller.randomize() #randomize config time values
        if br.search(sites,controller): #search a random site, if returns true, session time has run out
            br.close()
            if br.currentstartup >= startups: break #if reached the startups limit, break the loop
            print(str(datetime.datetime.now()) + " - resting for " + str(controller.breaktime) + ' '+controller.timeUnitString) 
            time.sleep(controller.breaktime)
            br.open(wbrowser)
            controller.resetTimer() #restarts the "stopwatch" to know when to exit the browser
    
print("reached " + str(startups) + " startups. closing...")