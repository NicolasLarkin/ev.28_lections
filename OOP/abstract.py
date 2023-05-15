'''
Абстракция
'''
# Абстракция (Абстрактый класс) - это принцип ООП, в котором создаются абстрактный класс (класс - пустышка),
#  т. е. в котором задаются названия атрибутов и методов для того чтобы мы могли их переопределить в дочерних классах
# (У нас есть название, но нет логики)

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):
#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
#         ...

# # class Cat(AbstractAnimal):
# #     legs = 4
# #     def voice(self):
# #         print('Гавб гав!')

# class Liion(AbstractAnimal):
#     legs = 4
#     def voice(self):
#         print('Гавб гав!')
# obj = Liion()

# print(obj.legs)


    
# class Dog(AbstractAnimal):
    # ...

# class Dog(AbstractAnimal):
#     legs = 5
    
#     def voice(self):
#         print('Гавб гав!')
        

# # @abstractproperty - декоратор который требует переопределения

# obj = Dog()
# obj2 = Cat()

# arr = [obj, obj2]

# for i in arr:
#     i.voice()
#     print(i.legs)


# from abc import *

# class Shape(ABC):
#     def init(self, name) -> None:
#         self.name = name
        
#     @abstractclassmethod
#     def area(self):
#         ...
    
# class Square(Shape):
#     def init(self, length) -> None:
#         super().init('Square')
#         self.length = length
        
#     def area(self):
#         return self.length ** 2

# obj = Square(10)
# print(obj.area())

"""
1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает,
сколько гласных букв в слове, которое передается в качестве аргумента в методе count,

а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов. 
С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

!!!! 
Обязательное условие: если в классе A или B не переопределить метод count должна выйти ошибка
!!!!

"""
# from abc import ABC, abstractmethod

# class NoLogic(ABC):

#     @abstractmethod
#     def count(self, word):
#         ...

# class A(NoLogic):
#     def count(self, word:str):
#         ltrs = ['a','o','i','u','e','y']
#         a = [i for i in word if i.lower() in ltrs]
#         return len(a)

# class B(NoLogic):
#     def count(self, word:str):
#         ltrs = ['a','o','i','u','e','y']
#         word = word.replace(' ','')
#         a = [i for i in word if not i.lower() in ltrs]
#         return len(a)

# obj = A()
# print(obj.count('Salam Aleykum'))
# obj1 = B()
# print(obj1.count('Salam Aleykum'))

"""
2) Создайте 3 класса:
Bird, Animal, Plant
класс Bird должен иметь методы: fly(), grow(), sound(). Animal: sound(), run(), grow(). Plant: grow(), photosynthesize()
каждый метод должен просто принтить действие. Например: def fly(self): print('я лечу')
!!!!
Обязательное условие: использовать абстракцию. Если не переопределить общий метод должна выходить ошибка
!!!!!
"""

# from abc import abstractmethod, ABC

# class Liver(ABC):
#     @abstractmethod
#     def grow(self):
#         ...
# class Bird(Liver):

#     def fly(self):
#         print('Я лечу!')

#     def grow(self):
#         print('Я расту!')
    
#     def sound(self):
#         print('Я чирикаю!')

# class Animal(Liver):

#     def grow(self):
#         print('Я расту!')

#     def sound(self):
#         print('Я издаю звук уиуиу!')

#     def run(self):
#         print('Я бегу!')

# class Plant(Liver):

#     def grow(self):
#         print('Я расту!')
        
#     def photosinteze(self):
        # print('Я есть фотосинтез!')



#------------------------------------------------------------------------------------------------

# from abc import ABC, abstractmethod, abstractproperty

# class Planet(ABC): 
#     def __init__(self, orbit): 
#         self.orbit = orbit 

#     @abstractmethod
#     def get_age(self,earth_age):
#          ...

# class Mercury(Planet): 
#         def get_age(self, earth_age): 
#             return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет' 

# class Venus(Planet): 
#     def get_age(self, earth_age): 
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней' 
    
# class Jupiter(Planet): 
#     def get_age(self, earth_age): 
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов' 
    
# mercury = Mercury(88) 
# venus = Venus(225) 
# jupiter = Jupiter(12) 
# print(venus.get_age(20)) 
# print(jupiter.get_age(20)) 
# print(mercury.get_age(20))




