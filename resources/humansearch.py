import pyperclip
import pyautogui
from pynput.keyboard import *



pyperclip.copy('The text to be copied to the clipboard.')
spam = pyperclip.paste()

class explorer():
    def __init__(self,links:list) -> None:
        self.searchlinks = links
        pass