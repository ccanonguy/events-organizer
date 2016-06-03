import json

with open('venues.json') as ft:
	d = json.load(ft)

venues = {'names': [], 'sn': []}

for venue in d:
	venues['names'].append(venue['name'])
	venues['sn'].append(venue['short_name'])

for venue in venues['sn']:
	try:
		venues['sn'].remove('0')
	except:
		pass

with open('venues_updated.json', 'w') as ft:
	json.dump(venues, ft)
