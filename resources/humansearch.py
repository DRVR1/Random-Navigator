import pyperclip
import pyautogui
import pynput.keyboard as keyboard
from resources.config import *
import time
import subprocess
import os


stopwhile = False

def onpress(key):
    global stopwhile
    if key == positionGrabber:
        stopwhile = True
        

class human():
    
    def __init__(self) -> None:
        self.pos_close = (0,0)
        self.pos_open = (0,0)
        self.pos_navbar = (0,0)
    
    def waitForinput(self):
        global stopwhile
        lis = keyboard.Listener(on_press=onpress) 
        lis.start()
        while(True):
            if stopwhile == True: break
        stopwhile = False
        lis.stop()
    
    def humanclick(self,where):
        pyautogui.click(where.x,where.y)
        pass
    
    def humanopenclick(self,where):
        pyautogui.click(where.x,where.y)
        time.sleep(0.3)
        pyautogui.click(where.x,where.y)

    def humanDoubleclick(self,where):
        pyautogui.click(where.x,where.y)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

    def closeBrowser(self):
        print('human is closing browser...')
        self.humanclick(self.pos_close)
        print('human closed the browser!')

    def openBrowser(self):#TODO issue: linux doesnt register gnome mouse position. browser must be opened from shell
        print('human is opening browser...')
        
        if os.name == 'nt':
            self.humanopenclick(self.pos_open)
        else:
            proc = subprocess.Popen([openBrowserCommand],shell=True)
            os.system('exit')
            
        print('human opened the browser!')
        print('waiting ' + str(openingBrowserTime) + ' seconds before start...')
        time.sleep(openingBrowserTime)

    def selectNavbar(self):
        print('human is selecting navbar...')
        self.humanclick(self.pos_navbar)
        print('human selected navbar!')

    def paste(self,what:str):
        print('human is pasting link')
        pyperclip.copy(what)
        pyautogui.keyDown(pasteKeys[0])
        pyautogui.press(pasteKeys[1])
        pyautogui.keyUp(pasteKeys[0])

    def enter(self):
        print('human hit enter')
        pyautogui.press('enter')

    def learn(self,what): #1 close, 2 open, 3 navbar (cambia el dato self a cambiar, y la string impresa)
        if(what == 1):
            if os.name == 'nt':
                print('Put your cursor in the browser app (taskbar - launcher bar) (it must open with one click) and press: ' + str(positionGrabber))
                self.waitForinput()
                self.pos_open = pyautogui.position()
        if(what == 2):
            print('Put your cursor in the X to close the browser and press: ' + str(positionGrabber))
            self.waitForinput()
            self.pos_close = pyautogui.position()
        if(what == 3):
            print('Put your cursor your browser navigation bar and press: ' + str(positionGrabber))
            self.waitForinput()
            self.pos_navbar = pyautogui.position()

