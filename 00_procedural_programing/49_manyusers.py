users = {
	'aeinstein' : {
	'first' : 'albert'
	'last' : 'einstein',
	'location' : 'princeton'
	},
	'mcurie' : {
	'first' : 'marie',
	'last' : 'currie',
	'location' : 'paris'
	}
}
for username, user_info in users.items():
	print(f"\nUsername: {username}")
	fullname = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull Name: {fullname.title()}")
	print(f"\tLocation: {location.title}")