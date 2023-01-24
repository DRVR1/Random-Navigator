import pynput.keyboard as keyboard
#config 

#TIME (random intervals (from, to) in the selected time unit)
timeUnit = 1 # 1-seconds 2-minutes 3-hours
staytimeT = (5,5) #time it stays in a website
totaltimeT = (1,1) #time the browser is open before close
breaktimeT = (1,30) #how much to wait before re-open the browser

#Browser config
startups = 0 #times the browser will close and re-open again to simulate a break from browsing (if 0, it never closes)
wbrowser = 2 #1-chrome 2-firefox 3-edge  (only with botsearch=True) and the browser must be installed

#humansearch config
positionGrabber = keyboard.Key.ctrl_l #this is the key you press to teach the macro where the buttons are
pasteKeys = ('ctrl','v') #the key combination you use to paste text
openingBrowserTime = 10 #the time it takes to start the browser. if your system is slow, increase the value (time unit: seconds)

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
                                                                                 ^
                                                                                 I\\
                                                                                 I \\       ^
                                                                                 I  \\
                                                                            ^    I*--\\    ^  ^
███╗   ██╗ █████╗ ██╗   ██╗██╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗         I    \\
████╗  ██║██╔══██╗██║   ██║██║██╔════╝ ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗        I     \\
██╔██╗ ██║███████║██║   ██║██║██║  ███╗███████║   ██║   ██║   ██║██████╔╝        I______\\
██║╚██╗██║██╔══██║╚██╗ ██╔╝██║██║   ██║██╔══██║   ██║   ██║   ██║██╔══██╗   _____I__O______
██║ ╚████║██║  ██║ ╚████╔╝ ██║╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║    \     ( )     b
╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝  ^^^^^^^^^^^^^^^^^^^^
┌───────────────────────────┐
│ author: DRVR1             │
│ version: 0.2              │
└───────────────────────────┘
'''

# Only for linux users: due to pyautogui cant detect cursor position in the Desktop/launcher, the browser must
# be opened from bash (os.system('comand'))

openBrowserCommand = '~/Downloads/tor-browser-linux64-12.0.2_ALL/tor-browser/Browser/start-tor-browser' # Your bash command that opens your browser.
