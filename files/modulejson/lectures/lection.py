# JSON - JavaScript Object Notation 
# - единый текстовый формат данных, был создан для хранения и передачи данных между сервисами
# <filename>.json файл в формате JSON

# {
#     "id": 1,
#     "author": {
#     "name": "Ed Sheeran",
#     "age": 35
#     },
#     "title": "don't",
#     "feat": false

# }  ----- это JSON


# !!!!!!!!!!!
# js object == {key: value}
# py dict == {key: value}
# JSON == {key: value}

# Процессы Сериализации и Десериализации данных (конвертация)

# Сериализация (запись данных в JSON) - перевод из Python в JSON формат

# dump -записывает данные в файл формата JSON 
# dumps - записывает данные в текст формата JSON

# Десериализация - (чтение данных из JSON) это процесс перевода из JSON в Py dict

# load - функция которая считывает данные из файла JSONa 
# loads - функция которая считывает данные из  текста py 

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# процесс сериализацаии

# dict_= {
#     'name': 'John Snow',
#     'status': True,
#     'wife': False,
#     'children': None

# }
# print(dict_,  type(dict()))

# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text)
#       )
# import json
# with open('new.json', 'w') as file:
#     json.dump(dict_, file, indent = 4)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Десериализация
# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()
# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))

# import json
# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_, type(dict_))
#----------------------------------------------------------------
from urllib.request import urlopen
import json 
import pprint as pp # красивое оформление

url = 'https://randomuser.me/api'
json_data = urlopen(url)

# print(json_data, dir(json_data))

dict_ = json.load(json_data)
pp.pprint(dict_)











