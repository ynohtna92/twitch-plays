import os
import time
if os.name == 'nt':
    import win32com.client
    import win32con
    import win32gui
    import win32api
else:
    from subprocess import Popen

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

    # keymaps for windows and linux
    # if adding more keys remember to update the config filters to reflect these changes
    if os.name == 'nt':
        # Windows virtual-key codes list can be found here
        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
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
    else:
        keymap = {
            'up': ["Up"],
            'down': ["Down"],
            'left': ["Left"],
            'right': ["Right"],
            'a': ["a"],
            'b': ["b"],
            'start': ["Return"]
        }

    def enumHandler(self, hwnd, lParam):
      if self.windowTitle in win32gui.GetWindowText(hwnd):
        lParam.append(hwnd)

    def __init__(self, config):
        self.config = config
        if os.name == 'nt' and self.config['features']['post']:
            self.windowTitle = self.config['features']['windowTitle']
            winlist=[]
            win32gui.EnumWindows(self.enumHandler, winlist)
            self.HWND = winlist[0]
            win32gui.ShowWindow(self.HWND, win32con.SW_SHOWNORMAL)

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        if os.name == 'nt':
            if self.config['features']['focus']:
                shell = win32com.client.Dispatch('WScript.Shell')
                shell.AppActivate(self.config['features']['windowTitle'])
            if self.config['features']['post']:
                win32api.PostMessage(self.HWND, win32con.WM_CHAR, self.button_to_key(button), 0)
            else:
                win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
                time.sleep(.07) # Minimum amount of time it takes for the key to register - adjust if nessessary
                win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            Popen(["xdotool", "keydown"] + self.button_to_key(button))
            time.sleep(.15) # Untested value - adjust if nessessary
            Popen(["xdotool", "keyup"] + self.button_to_key(button))
