# class methods, instance method, static methods.

'''isinstance methods - обычные методы, которые принимают первым аргуентом self (ссылка на объект). 
Нужны чтобы внутри метода мы могли работать с атрибутами объекта, получать их или изменять'''

# class Test:
#     def instance_method(self, a):
#         print('метод объекта')
#         print('первый аргумент:', self)

# obj = Test()
# obj1 = Test()
# obj.instance_method(5) #если вызвать у объекта, то el передается автоматически
# Test.instance_method(obj, 5) # если вызвать у класса, то в self нужно передать объект вручную
# obj1.instance_method(5)
#--------------------------------------------------------------------------------------------------------------
# class methods - методы, которые принимают первым аргументом cls(ссылка на класс). 
# Нужны для создания или изменения аттрибута и ддля манипуляций с классом внутри метода. Создается при помощи декоратора @classmethod

# class Test:

#     @classmethod
#     def class_method(cls, a):
#         print('It was method of the class')
#         print('first argument:', cls)

# obj = Test()
# print(Test(), '!!!')
# print()
# obj.class_method(5)
# print()
# Test.class_method(5)


# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self.a = 4

# obj_1 = C()
# obj_2 = C()
# obj_3 = C()
# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_3.counter)
# obj_1.counter += 1
# print()
# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_3.counter)
# C.counter += 5
# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_3.counter)


# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()
#         self.a = 4

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1
# obj1 = C()
# obj2 = C()
# obj3 = C()
# print(obj3.counter)
# obj4= C()
# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)

#-------------------------------------------------------------------------------------\\

# class Pizza:
#     def __init__(self, radius, *ingredients) -> None:
#         self.r = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f'Готовится пицца c размером {self.r * 2} cm')
#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r, 'peperonni', 'gribi', 'mocarella')
#         return pizza
#     def __str__(self) -> str:
#         return  f'{self.r} cm ->' + ', '.join(self.ingredients)
    
# pizza10 = Pizza(20, 'peperonni', 'gribi', 'mocarella')
# # pizza2 = Pizza(15, 'mocarella', 'darblyu', 'brinza')
# # pizza1 = Pizza(20, 'peperonni', 'gribi', 'mocarella')
# # pizza2 = Pizza(15, 'mocarella', 'darblyu', 'brinza')
# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza.four_cheese(20)
# pizza4 = Pizza.four_cheese(15)
# pizza1 = Pizza.four_cheese(20)
# pizza5 =Pizza(20,'mocarella', 'darblyu', 'brinza')


# print(pizza1)

# print(pizza2)

# print(pizza3)

# print(pizza4)

# print(pizza5)

#-------------------------------------------------------------------------

# class Person:

#     surname = 'Stark'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'Name: {self.name} {self.surname} -> Age: {self.age}')
#     @classmethod
#     def from_birth_year(cls, name, birth_date):
#         from datetime import date
#         age = date.today().year - birth_date
#         return cls(name, age)

# obj = Person('John', 24)
# print()
# obj.info()
# obj2 = Person('Arya', 14)
# print()
# obj2.info()
# obj3= Person.from_birth_year('Rob', 1996)
# obj3.info()

# from datetime import datetime, date
# a = datetime.now()
# print(a.strftime('%H:%M:%S'), type(a))  #формат показа времени !!! time delta(go internet)  находить разницу
#-------------------------------------------------------------
#staticmethod - это те методы в классе которые не принимают вв качестве аргументов 
# ни класс ни объект, так называемые методы которые не изменяют состояние

# class C:
#     @staticmethod
#     def static_method(a):
#         print('Статический метод!')
#         print(a)

# obj = C()
# obj.static_method(5)
# C.static_method(5)

# class Cylinder:
#     def __init__(self, radius, height) -> None:
#         self.area = self.get_area(radius, height)

#     @staticmethod
#     def get_area(r, h):
#         from math import pi
#         circle = pi * r**2
#         side = pi * h * (r * 2)
#         area = circle * 2 + side
#         return round(area, 2)
    
# obj = Cylinder(10, 7)
# print(f'Area: {obj.area}')

# obj1 = Cylinder(3, 12)
# print(f'Area: {obj1.area}')
#---------------------------------------------------------------------------------------------
"""
1) # Напишите класс CustomNumber, который принимает одно число и будет выполнять ту или иную операцию с ним.
# Перезапишите магические методы этих операторов
# Оператор сложения (+) будет выполнять функцию оператора  вычитания (-) и наоборот
# Оператор умножения (*) будет выполнять функцию оператора деления (/) и наоборот
# Так же перезапишите функционал операторов сравнения на противоположные (>, < ,==, !=)

# Вывод:
# num1 = CustomNumber(10)
# num2 = CustomNumber(5)

# print(num1 + num2)  # 5
# print(num2 - num1)  # 15
# print(num1 * num2)  # 2.0
# print(num2 / num1)  # 0.5

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 > num2)   # False
# print(num1 < num2)   # True
# print(num1 >= num2)  # False
# print(num1 <= num2)  # True
"""
class CustomNumber:

    def __init__(self, number):
        self.number = number
        
    def __add__(self, other):
        print('add call')
        if isinstance(other, CustomNumber):
            return self.number - other.number
        if isinstance(other, (int, float)):
            return self.number - other
        
    def __radd__(self, other):
        print('radd call')
        return self - other
       
    def __sub__(self, other):
        print('sub call')
        if isinstance(other, CustomNumber):
            return self.number + other.number
        if isinstance(other, (int, float)):
            return self.number + other
        
    def __rsub__(self, other):
        print('rsub call')
        return self + other
       
    def __mul__(self, other):
        print('mul call')
        if isinstance(other, CustomNumber):
            return self.number / other.number
        if isinstance(other, (int, float)):
            return self.number / other
        
    def __rmull__(self, other):
        print('rmull call')
        return self / other
        
    def __truediv__(self, other):
        print('truediv call')
        if isinstance(other, CustomNumber):
            return self.number * other.number
        if isinstance(other, (int, float)):
            return self.number * other
        
    def __rtruediv__(self, other):
        print('rtruediv call')
        return self * other
    
    def __eq__(self, other, other2):
        if other == other2:
            return True
        

num1 = CustomNumber(10)
num2 = CustomNumber(5)       
print(num1 + num2)
print(num2 - num1) 
print(num1 * num2)  
print(num2 / num1)  

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 > num2)   # False
# print(num1 < num2)   # True
