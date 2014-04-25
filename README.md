Twitch Plays (forked by ynohtna92)
==================================

Look alike of [Twitch Plays Pokemon](http://twitch.tv/twitchplayspokemon).

Windows, OSX and Linux

<p align="center">
  <img src="https://camo.githubusercontent.com/c75af50cf9fbbb206d7ec171d1a3925ba6ef3f9d/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f323234353331382f323234333530322f62643330356564322d396432632d313165332d393733642d3237636633393830646361372e706e67" alt="Demonstration broadcasting object">
</p>

Installation
============

**Dependencies**

* You're going to need to have (**Windows Only**) [pywin32](http://sourceforge.net/projects/pywin32/) installed. If you run into any errors try running this with (**Linux/OSX Only**)Python [2.7.x](http://www.python.org/download/releases/2.7/).

* [irc 8.5.4](https://pypi.python.org/pypi/irc) - IRC Client

* [Tornado](http://www.tornadoweb.org/en/stable/) - WebSocket Server

* (**Linux/OSX Only**) xdotool `apt-get install xautomation` 


Replace the username/password in the `config/config.py` file with your Twitch username and [OAuth token](http://www.twitchapps.com/tmi/). Feel free to modify the button toggles among other configuration options.

In your VBA/Emulator on windows, set the controls to the following -

```python
Up: 0
Down: 1
Left: 2
Right: 3
Button A: 4
Button B: 5
Start: 6
Select: 7
```
Keymaps for windows linux are listed in game.py and can be changed there. 

After you've set that up, open up your terminal in the correct directory and type `C:\Python27\python.exe twitchplays.py`.

Whilst the script is running **make sure you have your emulator in focus as your primary window**. If you click onto another window, the script won't work. If you're not able to stay focused on one window as you need to do other things with your computer, you could try running all of this from within a virtual machine.

Optionally you can use the postmessage option to send input commands. (Only works with some emulators)

If you are using linux there may be an option in the program to recieve background inputs. 


You can view the broadcast page which can be freely modified using the provided template. 
The page is hosted at `127.0.0.1:8888` while running the script. 
It is updated live and can be broadcasted using regions on your broadcasting software to surround the black box.


--

If you have any question or need help, feel free to [message me on Twitch](http://www.twitch.tv/message/compose?to=aidraj_) or send an email to `aidraj0 at gmail dot com`.

Alternatively message the owner of this fork at [Twitch](http://www.twitch.tv/message/compose?to=anth92).

Known Issues
------------

- No underscore character made in the Pokemon GB font causing weird spacing.
