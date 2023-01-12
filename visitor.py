from selenium import webdriver
import random
import time

#config section
staytime = random.randint(1,5) #random interval of time it stays in a website in seconds (from, to) 
driver = webdriver.Chrome() #you can change Chrome to Firefox or whatever
sitesfile = 'randomsites.txt' #list of websites (you can use generator.py to generate a list of random links inside a webpage or wepages you choose)


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


def gosearch(sitesvisited=0):
    print('====================================================')
    print('====================================================')
    print('sites visited: '+ str(sitesvisited))
    index = random.randint(0,len(sites)-1)
    site = sites[index]
    print('index is: ' + str(index))
    print('site is: ' + str(site))
    print('size: '+ str(driver.get_window_size()))
    print('loading site...')
    driver.get(site)
    sitesvisited += 1
    print('loaded. staying: ' + str(staytime) + ' seconds')
    time.sleep(staytime)
    print('Going to somewhere...')
    gosearch(sitesvisited)


gosearch()