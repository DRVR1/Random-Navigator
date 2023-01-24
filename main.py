from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Union
import time
from timeit import default_timer as timer
import random
import fake_useragent
import datetime
import os
import sys
from resources import humansearch
from resources import config

if os.name == 'nt': #if OS is windows, change console font color
    os.system('color ' + config.fontcolor)

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear()
print(config.title)

print('Selenium uses your web driver to navigate. The human search, instead, uses macros to navigate.')
print('important: if you are using human search and linux, please focus another window when saving the cursor position.')
print('1. Selenium search\n2. Human search')
op = int(input('input: '))
if op == 1: config.botsearch=True
if op == 2: config.botsearch=False

#other config
sitesfile = 'randomsites.txt' #list of websites (you can use generator.py to generate a list of random links inside a webpage or wepages you choose)


def blockPrint(): #TODO: this doesnt work :/
    sys.stdout = open(os.devnull, 'w')
def enablePrint():
    sys.stdout = sys.__stdout__

def printTime(aTime:float)->float: 
    if(config.timeUnit == 1):
        aTime =  aTime
    if(config.timeUnit == 2):
        aTime =  aTime/60
    if(config.timeUnit == 3):
        aTime = aTime/3600
    return round(aTime,3)


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
        
        self.loadedsites = 0

        self.staytime = 0
        self.totaltime = 0
        self.breaktime = 0
        self.startups = startups

        self.startTime = timer()

        if not config.botsearch:
            print('Dont move your browser window after saving cursor positions.\nMake sure your browser starts with the last size and position')
            self.human = humansearch.human()
            self.human.learn(1)
            time.sleep(1)
            self.human.learn(2)
            time.sleep(1)
            self.human.learn(3)

    def randomize(self):
        print("randomizing values...")
        self.staytime = random.uniform(self.staytimeT[0],self.staytimeT[1])
        self.totaltime = random.uniform(self.totaltimeT[0],self.totaltimeT[1])
        self.breaktime = random.uniform(self.breaktimeT[0],self.breaktimeT[1])
        

        if(config.timeUnit == 1):
            self.timeUnitString = 'seconds'

        if(config.timeUnit == 2):
            self.staytime = self.staytime*60
            self.totaltime = self.totaltime*60
            self.breaktime = self.breaktime*60
            self.timeUnitString = 'minute/s'

        if(config.timeUnit == 3):
            self.staytime = self.staytime*3600
            self.totaltime = self.totaltime*3600
            self.breaktime = self.breaktime*3600
            self.timeUnitString = 'hour/s'

        print("staying in website for: " + str(printTime(self.staytime)) + ' '+self.timeUnitString)
        print("open browser max time: "+ str(printTime(self.totaltime)) + ' '+self.timeUnitString)
        print("resting time: "+ str(printTime(self.breaktime)) + ' '+self.timeUnitString)
        print('loaded sites: ' + str(self.loadedsites))

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
        if(which==4):
            profile = webdriver.FirefoxProfile()
            #profile.set_preference('network.proxy.type', 1) #TODO obsolete 
            #opt = webdriver.FirefoxOptions()
            #opt.add_argument('network.proxy.type', 1)
            #opt.add_argument('network.proxy.socks', '127.0.0.1')
            #opt.add_argument('network.proxy.socks_port', 9050)
            #self.driver = webdriver.Firefox(profile,options=opt)
        return self.driver
    
    def close(self):
        self.driver.close()
        pass

    def selectsite(self,sites:list):
        index = random.randint(0,len(sites)-1)
        site = sites[index]
        return site
    
    def getsite(self,site:str,controller:Controller):
        if(config.botsearch):
            blockPrint()
            self.driver.get(site) #TODO disable print
            enablePrint()
        else:
            controller.human.selectNavbar()
            controller.human.paste(site)
            controller.human.enter()


    def rest(self,controller:Controller,driver=None): #

        if(config.botsearch):
            self.close()
        else:
            controller.human.closeBrowser()

        if self.currentstartup >= config.startups: return True #if reached the startups limit, break the loop by returning true
        print(str(datetime.datetime.now()) + " - resting for " + str(printTime(controller.breaktime)) + ' '+controller.timeUnitString) 
        time.sleep(controller.breaktime)

        if(config.botsearch):
            self.open(config.wbrowser) 
        else:
            controller.human.openBrowser()
        self.currentstartup += 1

        controller.resetTimer() #restarts the "stopwatch" to know when to exit the browser

    def informAfter(self,site:str,controller:Controller):
        if(controller.startups != 0):
            print("startup: " + str(self.currentstartup) + '/' + str(controller.startups))
        print('Total visited sites: ' + str(self.searchedsites))
        print("loading: "+site)
        pass

    def informpost(self):
        print(str(datetime.datetime.now()) + " - loaded, staying: " +str(printTime(controller.staytime)) + ' '+controller.timeUnitString)
        pass

    def search(self,sites:list,controller:Controller):
        site = self.selectsite(sites)
        self.searchedsites += 1
        self.informAfter(site,controller)
        self.getsite(site,controller)
        self.informpost()
        return self.betterSleep(controller.staytime,controller)#if betterSleep is interrupted by the max browsing time, returns true. otherwise returns false

    def close(self):
        print("closing browser... this may take some seconds depending on the browser")
        self.driver.close()

    def betterSleep(self,seconds:float, controller:Controller)->bool:
        counter = 0
        while(counter < seconds):
            counter += 1
            currentTime = timer()
            elapsedTime = currentTime - controller.startTime
            print('Website time: ' + str(printTime(counter)) + ' '+controller.timeUnitString + ' --- Open browser time: ' + str(printTime(elapsedTime)) + ' '+controller.timeUnitString, end='\r')
            if(elapsedTime > controller.totaltime):
                return True 
            time.sleep(1)
        return False



#get data from the file
sites = []
f = open(sitesfile,'r')
lines = f.readlines()
ldsites = 0
for line in lines:
    ldsites += 1
    sites.append(line)
f.close()


controller = Controller(config.staytimeT,config.totaltimeT,config.breaktimeT,config.startups)
controller.loadedsites = ldsites
controller.randomize()

br = Browser(controller)
if(config.botsearch):
    br.open(config.wbrowser)

print('starting')
if(config.startups == 0):
    while(True):
        br.search(sites,controller)
        controller.randomize()
else:
    while(True):
        clear()
        print("===========================================")
        controller.randomize() #randomize config time values
        if br.search(sites,controller): #search a random site, if returns True, browsing time has run out and browser should be closed
            if(config.botsearch):
                if (br.rest(controller,br.driver)): break 
            else:
                if (br.rest(controller)): break 


    
print("reached " + str(config.startups) + " startups. closing...")
