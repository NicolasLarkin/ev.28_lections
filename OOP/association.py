'''Ассоциация - принцип ООП, в котором два класса связаны друг с другом. 
Связь обозначает то что внутри одного объект будет существовать другой объект другого класса'''
# агрегация - слабая связь
# композиция - сильная связь 

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:

#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         print(f'The color of the phone is {color}')
#         #когда мы создаем внутри класса объект от другого класса - композиция

# a = Iphone('red')
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a
# # при удалении Айфона вместе с ним удаляется и батарейка

# class Nokia:
#     def __init__(self,battery: Battery, color: str) -> None:
#         self.color = color
#         self.battery = battery
#         #когда объект создается из вне класса и передается внутрь - агрегация

# battery =Battery()
# nokia1 = Nokia(battery, 'gray')
# print()
# print(nokia1.battery._power)
# del nokia1

# nokia2 = Nokia(battery, 'black')
# при удалении оъекта Нокия, батарейка остается

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Композиция 
# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type}'
    
# class Room:
#     def __init__(self):
#         self.west_wall = Wall('You entered West gate')
#         self.east_wall = Wall('You entered East gate')
#         self.south_wall = Wall('You entered South gate')
#         self.north_wall = Wall('You entered North gate')

# obj = Room()
# print(obj.west_wall)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Агрегация
# class Stream:
#     def __str__(self) -> str:
#         return 'Stream object'
    
# class Logger:
#     def __init__(self, stream) -> None:
#         self.stream = stream

#     def print_the_logs(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream')

# stream1 = Stream()
# logger1 = Logger(stream1)
# logger2 = Logger(stream1)
# logger = Logger(stream=Stream())

# logger1.print_the_logs()
# logger2.print_the_logs()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# class Engine:
#     country = 'Germany'

#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Power: {self.power}'
    
# class AudiCar:
#     brand = 'Audi'
#     country = 'Deutschland'

#     def __init__(self, model, power) -> None:
#         self.engine = Engine(power)
#         self.model = model

#     def __str__(self) -> str:
#         return f'{self.brand} {self.model} -> Engine: {self.engine} -> engine country: {self.engine.country}\n\nMade in {self.country}'


# car = AudiCar('A8', 400)

# print(car)




# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         print(self.name, self.memory)

#     def charge(self,percent):
#         self.battery += percent


# class Iphone(SmartPhones):

#     def send_message(self):
#         pass

# class Samsung(SmartPhones):

#     def show_time(self):
#         pass

# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone)
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 

#----------------------------------------------------------------------

# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         print(self.name, self.memory)

#     def charge(self,percent):
#         self.battery += percent


# class Iphone(SmartPhones):
#     ios = True
#     def send_message(self, word):
#         !!!!!!!!!!
#         print(f'Sending {word} from {obj.name}')

# class Samsung(SmartPhones):
#     android = True
#     def show_time(self):
#         from datetime import datetime
#         return datetime.now()


# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone)
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 


#--------------------------------------------------------------------
# class SmartPhones: 
#     def __init__(self, name, color, memory): 
#         self.name = name
#         self.color = color 
#         self.memory = memory 
#         self.battery = 0

#     def __str__(self): 
#         return f"{self.name} {self.memory}" 
    
#     def charge(self, number): 
#         self.battery += number 

# class Iphone(SmartPhones): 
#     def __init__(self, name, color, memory, ios): 
#         super().__init__(name, color, memory) 
#         self.ios = ios 

#     def send_imessage(self, string): 
#         return f"sending {string} from {self.name} {self.memory}" 
    
# class Samsung(SmartPhones): 

#     def __init__(self, name, color, memory, android): 
#         super().__init__(name, color, memory) 
#         self.android = android 

#     def show_time(self): 
#         import datetime 
#         return datetime.datetime.now().time()
     
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7) 
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())

#--------------------------------------------------------------------------------
