config = {
	
	'irc': {
		'server':'199.9.252.26',
		'channel':'#twitchplayspokemon',
		'port': 6667
	},

	'account': {
		'username': 'username',
		'password': 'oauth:' # get this fromm http://twitchapps.com/tmi/
	},

	'features': {
		'post': False,						# Use PostMessage instead of emulating the keyboard. (Only works for some emulators/games)
		'focus': True, 						# Focus a window containing the windowTitle below before sending a keypress.
		'windowTitle': "VisualBoyAdvance"	# Window title used for PostMessage and focusing.
	},

	# List of commands to filter
	# if adding more keys remember to update the game.py keymaps to reflect these changes
	'commands': [
		'a', 'b', 'left', 'right', 'up', 'down', 'start', 'select', 'democracy', 'anarchy'
	],

	# These commands will not be sent to the buttom feed or poll.
	'filted_commands': [
		'anarchy', 'democracy'
	],

	# Delete or comment out the following if you do not want to throttle buttons
	# The number represents seconds between consecutive button presses
	'throttled_buttons': {
		'start': 10 
	},

	# Enables polling mode (Democracy)
	'polling': {
		'enabled': False,
		'time': 10 # time in seconds
	},

	'anarchy-democracy': {
		'enabled': True, # This will initate into anarchy mode. Also overrides polling mode enabled flag.
		'size': 1000 # size of vote pool. The larger, the slower it will move, adjust according to how many viewers you have.
	}

	# To change the web app displayed time go to line 190 of \lib\template\index.html 
	# and replace the 10 digit value with your chosen epoch start time
}