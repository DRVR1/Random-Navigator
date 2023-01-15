
## fixing: 

hours are displayed in seconds

open browser time limit should interrupt website time limit 

# USAGE

1) Grab a lot of websites you would like to "visit", that has some HREF (links) in their's HTML code

2) list those websites in the file "inputsites.txt" (the "/" at the end of the URL doesnt matter)

3) execute: python generator.py

4) there will be generated a file called "randomsites.txt" that has a list of all the links displayed inside the before listed sites.

5) open and configure main.py

6) execute: python main.py

## what is navigator?
navigator is a bot, that uses your browser to search all those sites one by one, before visiting another site.

## Why would you need this?

To simulate browsing activity, in random or not random websites.

When using a vpn, this adds a layer of privacy, getting difficult to hackers from using an end-to-end confirmation attack. Be wise selecting your websites.

## what config is avaliable?

### config section of main.py:

browser = 1-chrome, 2-firefox, 3-edge

staytime_ = random interval of time it stays in a website in seconds (from, to) 

totaltime_ = time the browser is open before close

breaktime_ = how much to wait before re-open the browser

startups = times the browser will close and re-open again to simulate a break from browsing (if 0, it never closes)

randomUseragent = False #use another user agent?

sitesfile = 'randomsites.txt' #list of websites (you can use generator.py to generate a list of random links inside a webpage or wepages you choose)


# Requirements: 

bs4==0.0.1

requests==2.28.2

selenium==4.7.2

fake-useragent==1.1.1

