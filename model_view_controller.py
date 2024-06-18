import basic_backend
import mvc_exceptions as mvc_exc


class ModelBasic(object):

    def __init__(self, application_items):
        self._item_type = 'product'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, name, price, quantity):
        basic_backend.create_item(name, price, quantity)

    def create_items(self, items):
        basic_backend.create_items(items)

    def read_item(self, name):
        return basic_backend.read_item(name)

    def read_items(self):
        return basic_backend.read_items()

    def update_item(self, name, price, quantity):
        basic_backend.update_item(name, price, quantity)

    def delete_item(self, name):
        basic_backend.delete_item(name)


class View(object):

    @staticmethod
    def show_bullet_point_list(item_type, items):
        print(f'--- {item_type.upper()} LIST ---')
        for item in items:
            print(f'* {item}')

    @staticmethod
    def show_number_point_list(item_type, items):
        print(f'--- {item_type.upper()} LIST ---')
        for i, item in enumerate(items):
            print(f'{i+1}. {item}')

    @staticmethod
    def show_item(item_type, item, item_info):
        print('//////////////////////////////////////////////////////////////')
        print(f'Good news, we have some {item.upper()}!')
        print(f'{item_type.upper()} INFO: {item_info}')
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err):
        print('**************************************************************')
        print(f'We are sorry, we have no {item.upper()}!')
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        print('**************************************************************')
        print(f'Hey! We already have {item.upper()} in our {item_type} list!')
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        print('**************************************************************')
        print(f'We don\'t have any {item.upper()} in our {item_type} list. Please insert it first!')
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, item_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'Hooray! We have just added some {item.upper()} to our {item_type} list!')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change item type from "{older}" to "{newer}"')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change {item} price: {o_price} --> {n_price}')
        print(f'Change {item} quantity: {o_quantity} --> {n_quantity}')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(name):
        print('--------------------------------------------------------------')
        print(f'We have just removed {name} from our list')
        print('--------------------------------------------------------------')
