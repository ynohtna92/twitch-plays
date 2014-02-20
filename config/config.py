config = {
	
	'irc': {
		'server':'199.9.252.26',
		'channel':'#twitchplayspokemon',
		'port': 6667
	},

	'account': {
		'username': 'user',
		'password': 'oauth:' # get this fromm http://twitchapps.com/tmi/
	},

	'start_throttle': {
		'enabled': True,
		'time': 10 # time in seconds
	},

	'polling': {
		'enabled': False,
		'time': 4 # time in seconds
	}

}