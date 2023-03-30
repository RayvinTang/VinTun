favorite_language = {
	'jen' : 'python',
	'sarah' : 'c++',
	'edward' : 'ruby',
	'alex' : 'lua',
	'mike' : 'python'
}

print(favorite_language.items())

for name, language in favorite_language.items():
	print(f"{name.title()}'s favorite_language is {language.title()}")
for name in sorted(favorite_language.keys()):
	print(f"{name.title()}, thank you for taking the poll")

my_list = ['a', 'b', 'c', 'a']
print(set(my_list))

for language in sorted(set(favorite_language.values())):
	print(f"{language}")