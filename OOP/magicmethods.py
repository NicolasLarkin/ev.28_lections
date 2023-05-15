# magic methods (магические методы)
# dunder methods (double underscore) -> __init__
# служебные методы

'''Магия(фишка) заключается в том что эти методы запускаются без прямого обращения к ним, 
определеные методы могут отвечать за определенные операторы'''

# class A(int):
#     pass
# obj = A()
# print(len(dir(obj)))
#-----------------------------------------------------------------------------------------
# Магические методы сравнения 
# __eq__(self, other) -> 5 == 8
#                        5.__eq__(8)

# __ne__ -> !=

# __lt__ -> <

# __gt__ -> >

# __le__ -> <=

# __ge__ -> >=

# print('15' < 'ABC')
# print(ord('1'), ord('A'))

class Word(str):
    def __new__(cls, obj):
        # print(cls, '!!!')
        # print(obj, '!!!')
        obj = obj.replace(' ','')
        return super().__new__(cls, obj)
    
    def __init__(self) -> None:
        super().__init__()
        self.obj 
    
    def __gt__(self, other) -> bool:
        print('gt сработал')
        print(self)
        print(other)
        if len(self) > len(other):
            return self
        elif len(other) > len(self):
            return other
        else:
            return 'eq'

    def __lt__(self, __value):
        return len(self) < len(__value)
    

    def __eq__(self, __value: object) -> bool:
        return len(self.obj) == len(__value.obj)
obj = Word('Hllo ')

obj1 = Word('      m A k  E    rs')
print(obj > obj1)
print(obj < obj1)
print(obj == obj1)
#------------------------------------------------------------------
# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__ python2 -> __div__
# % -> __mod__
# ** -> __pow__
#------------------------------------------------------------------

# class Cifra:
#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance
    

#     def __add__(self, other):
#         print('add вызвана')
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')

# value1 = Cifra(-87)
# value2 = Cifra(53)
# value1 + value2
#-------------------------------------------------------------------
# from random import choice

# class Dog:
#     def sound(self):
#         print('Bark!')

# class Cat:
#     def sound(self):
#         print('Meow, meow!')

# class Lion:
#     def sound(self):
#         print('Roar!')
        
# class Pet:
#     def __new__(cls):
#         other = choice([Dog,Cat,Lion])
#         instance = super().__new__(other)    
#         print(f'I\'m {type(instance).__name__}')    
#         return instance
    
#     def __init__(self) -> None:
#         print('Pet never was called!')

# pet = Pet()
# pet.sound()

#---------------------------------------------------------------------

# SINGLETON

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self) -> str:                                # needed to change from data language to alphabet
#         return str(id(self))
    
# a = Singleton()
# b = Singleton()
# print(a)
# print(b)
# print(a is b)
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# дандер методы строкового отображения объектов 
# __str__
# __repr__ 

# class Base:
#     def __init__(self, stroka) -> None:
#         self.string = stroka
    
#     def __str__(self) -> str:
#         return f'Объект: {self.string}'
    
#     def __repr__(self) -> str:
#         return "Base('Example')"

# obj = Base('Jassy')
# print(obj)
# print(repr(obj))
# obj3 = eval(repr(obj))
# print(obj3)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coins(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)
    
#     def __getitem__(self, index):
#         return self.coins[index -1]


# obj = Kopilka()
# obj.add_coins(10)
# obj.add_coins(5)
# obj.add_coins(3)
# obj.add_coins(600)
# print(obj.total)
# print(obj.coins)
# print(len(obj.coins))
# print(obj[1])

# for x in obj:
#     print(x)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# """
# 1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

# У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

# Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

# в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

# класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

# класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

# класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
# """
        
        