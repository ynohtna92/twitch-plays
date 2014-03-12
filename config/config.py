config = {
	
	'irc': {
		'server':'199.9.252.26',
		'channel':'#twitchplayspokemon',
		'port': 6667
	},

	'account': {
		'username': 'anth92',
		'password': 'oauth:rmaz3oz4rwl7xt887wf9sme4wpexm6a' # oauth:aku9ihj1apk3n626pxgmyaal3cavz6d # get this fromm http://twitchapps.com/tmi/
	},

	'post': {
		'enabled': False, 					# Use PostMessage instead of emulating the keyboard. 
		'windowTitle': "VirtualBoyAdvance"	# This will allow you to send keyboard commands to a minimised window.
	},		  								# Only works for some games / emulators.

	'start_throttle': {
		'enabled': False,
		'time': 10 # time in seconds
	},

	'polling': {
		'enabled': False,
		'time': 10 # time in seconds
	},

	'anarchy-democracy': {
		'enabled': True, # This will initate into anarchy mode. Also overrides polling mode enabled flag.
		'size': 1000, # size of vote pool. The larger, the slower it will move, adjust according to how many viewers you have.
		'show': True # Determine whether to show anarchy/democracy chat commands in stream.
	},

	'controls': {
		'a': 0
	}
}