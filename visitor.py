from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time
from timeit import default_timer as timer
import fake_useragent

#config section
# 1 hour = 3600 seconds
#the time is in seconds (random number within the interval)
browser = 1 # 1-chrome, 2-firefox, 3-edge
staytime_ = [2,4] # random interval of time it stays in a website in seconds (from, to) 
totaltime_ = [5,5] #time the browser is open before close
breaktime_ = [5,5] #how much to wait before re-open the browser
startups = 1 # times the browser will close and re-open again to simulate a break from browsing (if 0, it never closes)
randomUseragent = False #use another user agent?
sitesfile = 'randomsites.txt' #list of websites (you can use generator.py to generate a list of random links inside a webpage or wepages you choose)


options = Options()
options.add_argument("--no-sandbox") # Bypass OS security model, MUST BE THE VERY FIRST OPTION
options.add_experimental_option("excludeSwitches", ['enable-automation']);  #remove chrome is being controlled by automated test software
options.add_argument("start-maximized") # open Browser in maximized mode
options.add_argument("disable-infobars") # disabling infobars
options.add_argument("--disable-extensions") # disabling extensions
options.add_argument("--disable-gpu") # applicable to windows os only
options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems

if randomUseragent:
    ua = fake_useragent.UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}') #setting a random useragent

def openbrowser(browser):
    if(browser==1):
        driver = webdriver.Chrome(options=options)
    if(browser==2):
        driver = webdriver.Firefox()
    if(browser==3):
        driver = webdriver.Edge()
    return driver
driver = openbrowser(browser)


#end of config section

staytime = 69
totaltime = 69
breaktime = 69
def randomize(): #time in seconds
    global staytime
    global totaltime
    global breaktime
    staytime = random.randint(staytime_[0],staytime_[1])
    totaltime = random.randint(totaltime_[0],totaltime_[1])
    breaktime = random.randint(breaktime_[0],breaktime_[1])
randomize()

print(driver.execute_script("return navigator.userAgent;"))


sites = []

try:
    f = open(sitesfile,'r')
except:
    print(sitesfile + ' not found, please add it in this same folder. Remember to execute the script from here')
lines = f.readlines()
for line in lines:
    print("readed line: " + line)
    sites.append(line)
f.close()

sitesvisited = 0


startTime = timer()

def gosearch(st,startups): #TODO global startups
        global sitesvisited
        randomize()
        print('====================================================')
        print('====================================================')
        print('startup: ' + str(st) + ' of ' + str(startups))
        print('sites visited: '+ str(sitesvisited))
        index = random.randint(0,len(sites)-1)
        site = sites[index]
        print('index is: ' + str(index))
        print('site is: ' + str(site))
        print('size: '+ str(driver.get_window_size()))
        print('loading site...')
        driver.get(site)
        print('loaded. staying: ' + str(staytime) + ' seconds')
        time.sleep(staytime)
        print('Going to somewhere...')
        sitesvisited += 1

        if(startups != 0): # if should close
            currentTime = timer()
            elapsed = currentTime - startTime #checks elapsed time
            if(elapsed>totaltime): #if time runs out
                print("elapsed time: " + str(elapsed))
                print("closing and reopening in " + str(breaktime) + ' seconds')
                startups += 1
                driver.close() # close the window
                return
            else:
                gosearch(st,startups)
        else:
            gosearch(st,startups)
        
#TODO randomize times

if(startups == 0): #infinite search
    gosearch()

st = 0
firstTime = True
while(st < startups):
    if firstTime:
        gosearch(st,startups)
        firstTime = False
    else: #TODO check break time
        time.sleep(breaktime)
        print("opening nav...")
        driver = openbrowser(browser)
        st+=1
        gosearch(st,startups)

print("\nfinished execution. exiting...\n")

