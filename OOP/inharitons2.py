# Множественное наследование - это когда класс наследуется от двух или более классов

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing!')
    
#     def ride(self):
#         print('We are riding on the ground!')
    

# class Plane:
#     def play_music_at_station(self):
#         print('Listening Ed Shiran...')

#     def fly(self):
#         print('We are flying!')

# class FutureAuto(Auto, Plane):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()
#----------------------------------------------------------------------------------------
# print(dir(object))
# MRO - method resolution Order
# Rhomb Problem
#-------------------------------------------------------------------------------------------
# Проблема ромба когда поиск шел в родительский класс прежде чем искать у соседнего общего потомка. Решена с помощью МРО
# MRO - механизм для корректного поиска родительских методов. Был создан для решения проблемы ромба, которая появилась после введения object в Python. 
# Поиск идет таким образом , что если  родительских классов есть общий предок, то поиск идет в ширину.

# class Zero:
#     def say(self):
#         print('Class Zero')

# class First:
#     def say(self):
#         print('Class First')

# class Second:
#     def say(self):
#         print('Class econd')

# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('Class MyClass')    

# obj = MyClass()
# obj.say()
# print(MyClass.mro())

# class Z: # 2
#     pass

# class Y: # 4
#     pass

# class B: #3
#     pass

# class A(Z): #1
#     pass

# class B(Y): 
#     pass

# class X(A,B):
#     pass

# print(X.mro())
#--------------------------------------------------------------------------------
# Проблема перекрестного наследования
# from typing import List
# class Y:
#     pass

# class X:
#     pass

# class A(Y,X):
#     pass

# class B(Y, X):
#     pass

# class MyMro(type):
#     def mro(cls) -> List[type]:
#         return [object, A, B, X, Y, object]
    
# class MyClass(A,B, metaclass=MyMro):
#     pass

# print(MyClass.mro())



