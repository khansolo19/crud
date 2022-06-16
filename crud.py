import requests

class CRUD:
    HOST = 'http://3.125.115.120/'

    def __init__(self) -> None:
        self.option = 'crud/products/'

    def get_url(self):
        return f'{self.HOST}{self.option}'

    def get_products_or_retrieve(self):
        id_ = input('Введите id продукта, который Вы хотите получить или пропустите, чтобы получить все продукты ')
        if not id_:
            req = requests.get(f'{self.get_url()}')
        else:
            req = requests.get(f'{self.get_url()}{id_}')
            while 'detail' in req:
                id_ = input('Такого id не существует. Введите другое значение ')
                req = requests.get(f'{self.get_url()}{id_}')
                if 'detail' not in req:
                    break
        return req.text

    def create_product(self):
        print('Создание продукта\n')
        data = {
            'title': input('Введите название '),
            'description': input('Введите описание '),
            'price': float(input('Введите цену '))
        }
        req = requests.post(f'{self.get_url()}', data=data)
        return req.text

    def update_product(self):
        id_ = input('Введите id продукта, который Вы хотите изменить ')
        obj = requests.get(f'{self.get_url()}{id_}').json()
        while 'detail' in obj:    
            id_ = input('Такого id не существует. Введите другое значение ')
            obj = requests.get(f'{self.get_url()}{id_}').json()
            if 'detail' not in obj:
                break
        data = {
            'title': input('Введите название или пропустите ') or obj['title'],
            'description': input('Введите описание или пропустите ') or obj['description'],
            'price': input('Введите цену или пропустите ') or obj['price']
        }
        req = requests.patch(f'{self.get_url()}{id_}/', data=data)
        return req.text

    def delete_product(self):
        id_ = input('Введите id продукта, который Вы хотите удалить ')
        obj = requests.get(f'{self.get_url()}{id_}').json()
        while 'detail' in obj:
            id_ = input('Такого id не существует. Введите другое значение ')
            obj = requests.get(f'{self.get_url()}{id_}').json()
            if 'detail' not in obj:
                break
        ans = input('Вы уверены? (да/нет) ').lower()
        if ans == 'да':
            req = requests.delete(f'{self.get_url()}{id_}/')
            return req.text
        else:
            return 'Отмена операции'
    



a = CRUD()
# print(a.get_products_or_retrieve())
# print(a.get_products_or_retrieve())
# print(a.create_product())
# print(a.update_product())
# print(a.delete_product())
print(a.get_products_or_retrieve())


# TODO: airtable
# TODO: отрефакторить код