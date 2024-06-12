import mvc_exceptions as mvc_exc

# global variable where we keep the data
items = list() 


def create_item(name, price, quantity):
	global items
	results = list(filter(lambda x: x['name'] == name, items))
	if results:
		raise mvc_exc.ItemAlreadyStored(f'{name} already stored!')
	else:
		items.append({'name': name, 'price': price, 'quantity': quantity})


def create_items(app_items):
	global items
	items = app_items


def read_item(name):
	global items
	my_items = list(filter(lambda x: x['name'] == name, items))
	if my_items:
		return my_items[0]
	else:
		raise mvc_exc.ItemNotStored(f'Can\'t read {name} because it\'s not stored!')


def read_items():
	global items
	return [item for item in items]


