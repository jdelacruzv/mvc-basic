# global variable where we keep the data
items = list() 


def create_items(app_items):
	global items
	items = app_items


def create_item(name, price, quantity):
	global items
	items.append({'name': name, 'price': price, 'quantity': quantity})


def read_items():
	global items
	return [item for item in items]


def read_item(name):
	global items
	my_items = list(filter(lambda x: x['name'] == name, items))
	return my_items[0]