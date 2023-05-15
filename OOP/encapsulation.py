# Инкапсуляция :
# 1. Языковая конструкция , которая помогает связать данные с методами для их обработки и управления 
# (связь между данными и методами которые управляют ими) (Capsula - капсула)
# 2. Механизм сокрытия, при помощи которого можно ограничить доступ одного компонента программы к другому

# Инкапсуляция как связь 

# class Phone:
#     number = '+996773500660'

#     def print_number(self):
#         print(f'Мой номер : {Phone.number}')
#         print(f'Мой номер : {self.number}')

# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как механизм сокрытия 
# 3 уровня скорытия данных в питоне 
#     1. Публичный (public) - number, print_number
#     2. Защищенный (_protected) - _number
#     3. Приватный (__private) - __number

# class Car:
#     _country = 'Germany'

#     def __init__(self) -> None:
#         self.marka = 'Mercedes-Benz' #Public
#         self.model = 'w140' # Protected
#         self.__color = 'Grey' # Private

# obj = Car()
# print(dir(obj))
# print(obj._Car__color)
# print(obj._country)
# print(obj.model)
#----------------------------------------------

# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 15
    
#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         question = input('взять трубку(yes/no): ')
#         if question.lower().strip() == 'yes':   
#             self.__turn_on()
#         else:
#             print('Сбросили трубку!')

#     def __increment_calls(self):
#         self.__count_of_calls += 1

#     def __turn_on(self):
#         self.__increment_calls()
#         print('Aloo!')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

# obj = Phone()
# print(obj.username)
# obj.call()
# obj.call()
# obj.call()
# obj.call()
# obj.call()
#-----------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name 
#         self.age = age 

#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old')

# obj = Person('M.O.', 18)
# print(obj.display_info())
# obj.nationality = 'Kyrgyz'
# print(obj.nationality)
# obj.age = -18
# obj.name = 55
# obj.display_info()

#------------------------------------------------------------------
# getter & setter
# Они нужны чтобы избежать прямого обращения к сокрытым атрибутам при этом можно 
# добавить логику валидации(проверки) данных которые будут установлены в атрибут.

class Person:
    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age 

    def display_info(self):
        print(f'My name is {self.__name} and I\'m {self.__age} years old')

    #getter
    def name(self):
        return self.__name
    
    #setter
    def set_name(self, name):
        if not isinstance(name, str):
            print('Name must be str object!')
        else:
            self.__name = name

    #getter
    def age(self):
        return self.__age
    
    #setter
    def set_age(self, age):
        if not isinstance(age, int) or not 0 <= age < 150:
            print('Invalid value for age!')
        else:
            self.__age = age

obj = Person('John', 24)
print(obj.name())
obj.set_age(-18)
obj.display_info()
obj.set_name('Malkolm')
obj.set_age(55)
obj.display_info()

# При помощи инкапсуляция можно будет ставить проверки таким образом чтобы в ячейки  
# Name не попадали цифры также в age не попадали минусовые значения итд
