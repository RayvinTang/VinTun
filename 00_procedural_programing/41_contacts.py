fav_lang = {
	'Adri' : 'C',
	'Alfons' : 'Swift',
	'Chelvi' : 'Golang'
}

contacts = {
	'jesse' : '0817335421',
	'justin' : '089965432112',
	'Rayvin' : '081323454321'
}

print(f"Rayvin' number phone is {contacts['Rayvin']}.")

rayvin = contacts.get('Rayvin')
print(rayvin)
mr_x = contacts.get('mr_x')
print(mr_x)
mr_y = contacts.get('mr y', 'no mr y')
print(mr_y)