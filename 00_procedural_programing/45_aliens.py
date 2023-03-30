aliens = []

for i in range(30):
	alien = {'color':'green', 'points':0}
	aliens.append(alien)
for alien in aliens[0:5]:
	print(alien)
print(f"Toatal number of aliens in {len(aliens)}")