from data_raw import *

data_refined = []

for item in data[:10]:
	b = {
			'name': item['name'],
			'short_name': item['short_name']
		}
	data_refined.append(b);

print data_refined