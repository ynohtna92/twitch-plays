import win32api
import win32con
import win32gui

import time

"""
Remap VBA/Emulator keys to the following.

Up: 0
Down: 1
Left: 2
Right: 3
Button A: 4
Button B: 5
Start: 6
Select: 7

"""

class Game:

    keymap = {
        'up': 0x30,
        'down': 0x31,
        'left': 0x32,
        'right': 0x33,
        'a': 0x34, 
        'b': 0x35,
        'start': 0x36,
        'select': 0x37
    }

    def enumHandler(self, hwnd, lParam):
      if self.windowTitle in win32gui.GetWindowText(hwnd):
        lParam.append(hwnd)

    def __init__(self, config):
        self.config = config
        if self.config['post']['enabled']:
            self.windowTitle = self.config['post']['windowTitle']
            winlist=[]
            win32gui.EnumWindows(self.enumHandler, winlist)
            self.HWND = winlist[0]
            win32gui.ShowWindow(self.HWND, win32con.SW_SHOWNORMAL)

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        if self.config['post']['enabled']:
            win32api.PostMessage(self.HWND, win32con.WM_CHAR, self.button_to_key(button), 0)
        else:
            win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
            time.sleep(.07) # Minimum amount of time it takes for the key to register - adjust if nessessary
            win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
