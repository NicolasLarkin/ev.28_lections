# Объектно-ориентированное программмирование 

# Класс --> это описание того как должен выглядеть объект, 
# то есть в классе мы описываем какими свойствами (данными) и поведением (функции) должен обладать объект

# Объект -->  это сущность которую мы создаем от класса, у объекта есть собственные состояние свойств(данные)

# Целью создания было свзать данные с функциями которые управляли этими данными.

# Свойства(атрибутами) - называют обычные переменные внутри класса в которых хранятся данные объекта. !!!(Переменные)

# Методы - это обычные функции внутри класса, методы описывают поведение объекта. !!!(Функции)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# class Human:
#     age = 0
#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizenship = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizenship}'

# john = Human('John', 'Snow', 'King of North', 'Northerner')
# bilal = Human('Bilal', 'Lannister', 'Programmer', 'KR')

# # print(john, type(john))
# # print(dir(john))
# print(john.show_info())
# john.job = 'King of Westeros'
# john.age = 24
# print(john.show_info())
# print()
# print(bilal.show_info())

# -= -=- =- = - -== - =-= - -=- = - =-=- =- -=
# class Dog:
#     # атрибуты класса
#     age = 0 
#     ushi = True

#     def __init__(self, name, color):
#         " Инициализатор, именно здесь создаются атрибуты объекта"
#         # self -ссылка на объект который только что создался
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Color: {self.color}, Ushi: {self.ushi}'

# rex = Dog('rex', 'black')
# pluto = Dog('pluto', 'brown')
# ak_tosh = Dog('Aktosh' ,'Gray')

# print(rex.show_info())
# print(pluto.show_info())
# print(ak_tosh.show_info())

# rex.age = 2
# pluto.age = 5
# ak_tosh.age = 3

# ak_tosh.ushi = False
# print(rex.show_info())
# print(pluto.show_info())
# print(ak_tosh.show_info())

# rex.bark()
# pluto.bark()

#==================================----------------------------==================================
# class Human:
#     def __init__(self):
#         print('Init worked')
#         self.raychel = 'raychel'
#         self.golod = 100

#     def eat(self, meal, doela=True):
#         print(f'{self.raychel} покушала {meal}')
#         if doela:
#             self.golod -= 50
#         else:
#             self.golod -= 25

# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat('burge', doela=False)
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)





