alien = {'color':'green', 'skill':'jumping'}
player = {'username':'yourbapak', 'points':1000, 'coins':5000}

print(alien['color'])
print(player['points'])

alien['x'] = 100
alien['y'] = 200

alien['color'] = 'tosca'
player['coins'] += 100

del player['coins']

print(alien)