import requests

class CRUD:
    HOST = 'http://3.125.115.120/'

    def __init__(self) -> None:
        self.option = 'crud/products/'


    def get_products_or_retrieve(self, id_:int =None):
        if not id_:
            req = requests.get(f'{self.HOST}{self.option}')
        else:
            req = requests.get(f'{self.HOST}{self.option}{id_}')
        return req.text

    def create_product(self):
        data = {
            'title': input('Введите название '),
            'description': input('Введите описание '),
            'price': float(input('Введите цену '))
        }
        req = requests.post(f'{self.HOST}{self.option}', data=data)
        return req.text

    def update_product(self, id_):
        obj = requests.get(f'{self.HOST}{self.option}{id_}')
        a = input('Что вы хотите поменять? ')
        req = requests.patch(f'{self.HOST}{self.option}{id_}', data=obj)
        return req.text
    



a = CRUD()
print(a.get_products_or_retrieve(4))
# print(a.create_product())


# TODO: дописать функционал
# TODO: airtable
# TODO: отрефакторить код