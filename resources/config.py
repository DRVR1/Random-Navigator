import pynput.keyboard as keyboard
#config 

#TIME (random intervals (from, to) in the selected time unit)
timeUnit = 1 # 1-seconds 2-minutes 3-hours
staytimeT = (3,7) #time it stays in a website
totaltimeT = (10,30) #time the browser is open before close
breaktimeT = (5,5) #how much to wait before re-open the browser

#Browser config
startups = 6 #times the browser will close and re-open again to simulate a break from browsing (if 0, it never closes)
wbrowser = 2 #1-chrome 2-firefox 3-edge  (only with botsearch=True) and the browser must be installed

#humansearch config
positionGrabber = keyboard.Key.ctrl_l #this is the key you press to teach the macro where the buttons are
pasteKeys = ('ctrl','v') #the key combination you use to paste text
openingBrowserTime = 3 #the time it takes to start the browser. if your system is slow, increase the value (time unit: seconds)

#Nice
fontcolor = 'C'  #console font color (windows only)
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



#title
title = '''
███╗   ██╗ █████╗ ██╗   ██╗██╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗
████╗  ██║██╔══██╗██║   ██║██║██╔════╝ ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██╔██╗ ██║███████║██║   ██║██║██║  ███╗███████║   ██║   ██║   ██║██████╔╝
██║╚██╗██║██╔══██║╚██╗ ██╔╝██║██║   ██║██╔══██║   ██║   ██║   ██║██╔══██╗
██║ ╚████║██║  ██║ ╚████╔╝ ██║╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
┌───────────────────────────┐
│ author: DRVR1             │
│ version: 0.1              │
└───────────────────────────┘
'''
