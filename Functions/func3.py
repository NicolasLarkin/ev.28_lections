# Встроенные функции
# Анонимная функция - lambda (обычная функция с одной особенностью у нее нет имени)
# Принимает сколько угодно параметров, но всегда возвращает одно выражение

# def hello():
#     return 'hello'
# print(hello())

# x = lambda: 'hello'
# print(x())

# x = lambda a, b, c:(a*  b) % c
# print(x(5,5,5))

# x(1,2,4) 

# x = lambda a, b, c=None: (a * b) ** c if c else a * b
# print(x(10,5))
# print(x(2,3,4))

# def myFunc(n):
#     return lambda num : num * n

# my_doubler = myFunc(2)
# # print(my_doubler(50))

# dict_= {
#     'john': 500,
#     'tirion' : 160_000,
#     'tom': 150,
#     'sancar': 20,
#     'ayana' : 100_000,
# }
# new_dict = dict(sorted(dict_.items(),key = lambda x:x[1],reverse=True))
# print(new_dict)

"""
map(function,iterable) - применяется к каждому элементу внутри iterable функцию, которую мы ей передаем в function, 
закидывая в результат те данные, которые возвращает функция. В результате мы получаем mapobject(iterator), в котором хранятся все наши данные.
"""

# ls = ['one', 'two','three','four']

# new_list = list(map(lambda x: x.capitalize(), ls))
# print(new_list)

# ls = ['1','2','3']
# new_list =list(map(int, ls))
# print(new_list)

# names = ['john', 'aria', 'baku', 'bakberdi', 'lilo']
# intro = list(map(lambda x: f'Hello mr/mrs {x}',names))
# print(intro)

'''
Функция высшего порядка - функция, 
которая принимает в качестве аргумента другую функцию
'''

# filter(function,iterable) - применяет ко всем элементам iterable фунцкию, 
# которую мы передали и возвращает filterobject(итератор) только с теми элементами, 
# для которых функция вернула True

# ls = ['one', 'twoo', 'oleg', 'bille', 'tirion']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)
'''
enumerate(iterable) - пронумеровывает каждый элемент внутри iterable ее собственным индексом
'''

# ls = ['str1', 'str2', 'str3']
# new_list = list(enumerate(ls))
# print(new_list)





























