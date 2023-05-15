from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin
import json

class Product(CreateMixin,ReadMixin,UpdateMixin,DeleteMixin):
    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4)
        return 'Saved'

class Comments(CreateMixin, ReadMixin, DeleteMixin):
    pass

smartphones = Product()
print(smartphones.post(title = 'Redmi Note 10', description='Wonderful!', qty=10, price=250))
print(smartphones.post(title = 'Redmi Note 20', description='The best phone for own price!', qty=5, price=500))
print(smartphones.post(title = 'Iphone 14 Pro Max', description='New cool and super phone!', qty=5, price=100))
print(smartphones.post(title = 'Samsung S22 Ultra', description='The invincible !!!!', qty=5, price=600))
print(smartphones.post(title = 'Iphone 12 Pro', description='Still the best!', qty=15, price=420))
print()
print()
print(smartphones.list())
print()
print(smartphones.detail(3))
print(smartphones.detail(15))
print()
print(smartphones.patch(1, title = 'Redmi Note 10'))
print()
print(smartphones.list())
print(smartphones.delete(-1))
print(smartphones.delete(1))
print(smartphones.save())

