import requests

class CRUD:
    HOST = 'http://3.125.115.120/'

    def __init__(self) -> None:
        self.option = 'crud/products/'

    def get_url(self):
        return f'{self.HOST}{self.option}'

    def get_products_or_retrieve(self):
        try:
            id_ = int(input('Введите id продукта, \nкоторый Вы хотите получить или пропустите, чтобы получить все продукты '))
        except ValueError:
            id_ = None
        if not id_:
            req = requests.get(f'{self.get_url()}')
        else:
            req = requests.get(f'{self.get_url()}{id_}/')
        return req.text

    def create_product(self):
        data = {
            'title': input('Введите название '),
            'description': input('Введите описание '),
            'price': float(input('Введите цену '))
        }
        req = requests.post(f'{self.get_url()}', data=data)
        return req.text

    def update_product(self):
        id_ = int(input('Введите id продукта, \nкоторый Вы хотите обновить '))
        obj = requests.get(f'{self.get_url()}{id_}/').json()
        try:
            data = {
                'title': input('Введите название или пропустите ') or obj['title'],
                'description': input('Введите описание или пропустите ') or obj['description'],
                'price': float(input('Введите цену или пропустите ')) or obj['price']
            }
        except ValueError:
            pass
        req = requests.put(f'{self.get_url()}{id_}/', data=data)
        return req.text
    
    def delete_product(self):
        id_ = int(input('Введите id продукта, \nкоторый Вы хотите удалить '))
        ans = input('Вы уверены? (y/n) ')
        if ans == 'y':
            req = requests.delete(f'{self.get_url()}{id_}/')
        else:
            print('Отмена операции')
        return req.text



a = CRUD()
print(a.get_products_or_retrieve())
print(a.create_product())
print(a.update_product())
print(a.delete_product())


# TODO: airtable
# TODO: отрефакторить код