# Декораторы -> это функция которая позволяет без изменения кода функции расширить ее функционал.

# def decorator(func):
#     print(func)
#     func()

# def hello():
#     print('Hello stranger!')

# def john():
#     print('My name is John Snow! I\'m King of North!')

# decorator(hello)
# print('!!!!!')


# decorator(john)

# pythonic way -> @
# Синтаксический сахар - красота кода

# def decorator(func):
#     def wrapper():
#         print(f'МЫ вызвали функцию: {func.__name__}')
#         func()
#     return wrapper

# @decorator   #@decorator -> decorator(hello)
# def hello():
#     print('Hello stranger!')

# @decorator
# def john():
#     print('My name is John Snow! I\'m King of North!')

# hello()
# print()
# john()

# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(*args,**kwargs)
#         finish = time.time()
#         print(f'Время выполнения функции: {func.__name__}, заняло {finish - start}.')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1

# @benchmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         ls.append(i)
#         i += 1
#     print(ls)

# add()
# loop()

# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args,**kwargs) + '</bold>'
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*args,**kwargs):
#         res = '<div>' + func(*args,**kwargs) + '<div>'
#         return res
#     return wrapper


# @bold
# def str_(name):
#     return name
# @bold
# def name(name, last_name):
#     return name +(" ")+ last_name

# print(str_('John Snow'))
# print(name('Jamie','Lannister'))

#----------------------------
def trace(func):
    def wrapper(*args,**kwargs):
        print(f'Trace вызвала {func.__name__}(),\nона приняла в себя args:{args}, kwags:{kwargs}')
        original_result = func(*args,**kwargs)
        print(f'Trace вызвала {func.__name__}(),\nона вернула:{original_result}')
        return original_result
    return wrapper

@trace
def say(name,adress):
    return f'{name} --> {adress}'

@trace
def hello(name,last_name,country):
    return f'Hello {name} {last_name} from {country}!'

say('Sherlok Holmes', 'Backery street 221B')
hello('Homer', 'Simpson','Canada')
























































































































