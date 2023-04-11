# dict()- Словарь - > упорядоченная коллекция элементов (python3.7 -> ordered). Каждый элемент внутри словаря хранится в виде пары :{ключ:значение}

# ассоциативный массив , hash table, object(js), structure == dictionary(py)

# ключами могут быть только неизменяемые типы данных и в словаре сохраняются только уникальные ключи.
# тогда как зачениями могут выступать любые типы данных.

# thisdict = {
#     'brand': 'Ford',
#     'model' : 'Mustang',
#     'year' : 1967
# }

# print(thisdict)
# print(type(thisdict))
# print(thisdict['model'], thisdict['brand'])
# print(thisdict['year'])

# thisdict['motor'] = 'GTE Turbo'
# thisdict['brand']= 'Tesla'
# print(thisdict)

# a = {1,2,3,4,5,6}
# print(type(a))

# a = {}
# b = dict()

# print(dir(dict))

# items, keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',
# }

# ls = user_info.keys()
# ls = list(ls)
# print(ls[2:])

# ls = list(user_info.values())
# print(ls)

# items = user_info.items() # Возвращает ключи и их содержимое
# print(items)

# print(user_info)
# for value in user_info.values():
#     print(value)

# for key in user_info.keys():
#     print(key)

# print(user_info)
# for x in user_info.items():
#     print(f'keys: {x[0]}, values: {x[1]}')

# dict_ = {'name': 'Jack', 'age': 17}
# print(dict_)
# dict_['name']= 'John'
# dict_['age'] = 24
# dict_['address'] = 'Winterfell'
# print(dict_)
# dict_.update({'age':25, 'address': 'Blackcastle'})
# print(dict_)
#---------------------------------------------------------

# получение данных со словаря 

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[2], '!!!')
# print(dict_.get(3))

# setdefault -> работает так же как и get, но если нет такого ключа то создаст новю пару из этого списка.
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(5, 'Mannty'))                             
# print(dict_)
# Если нет какого либо введенного ключа сетдефолт создаст ключ и значение
#--------------------------------------------------------------------------
# создание - fromkeys метод для создания быстрого словаря 
# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, 'Value')
# print(new_dict)
#--------------------------------------------------------------------------
# Удаление элементов 
# pop , popitem

# pop(<key>) - удаляет пару по ключу
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)

# popitem -> Удаляет последнюю пару
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed=dict_.popitem()
# print(dict_)
# print(removed)

#----------------------------------------------------------------------------
# roles = {
#     0:'Admin',
#     1:'Customer',
#     2:'Vendor',
# }

# users = {
#     1:{
#     'id':1, 'role': roles[2], 'username': 'Tirion',
#     },
#     2: {
    
#         'id': 2, 'role': roles[0] , 'username': 'John Snow',
#     },
#     3:
#       {
#     'id': 3, 'role': roles[1] , 'username': 'Raychel'
#       }
# }

# product = {
#     'id': 1,
#     'title':'Samsung Galaxy A51',
#     'description': 'Loren Ipsum',
#     'price': 250
# }
# print(users)
# print(product)

# id_user = int(input('Vvedite id:'))
# if users [id_user]['role'] == roles[0]:
#     product['description'] = input('Vvedite opinasiye:')
# else:
#     print('You do not have permissions!')

# print(product)





# n = {'a': None, 
#      'b': 1, 
#      'c': 2, 
#      'd': None, 
#      '': 3} 
# b = {key:value for key, value in n.items() if value} 


# b = {key: 'helo' for key, value in n.items() if key}

# print(b)









































