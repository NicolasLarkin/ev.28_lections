# Типы данных  -> int, float

# = -> оператор присваивания
# variable (переменная)
# num = 5
# print (num) #5
# num = 79 # переопределение
# print(num)  #79

# abc -> нижний регистр
# ABC -> Верхний регистр

# PEP8 
# tomorrow_day = '10.03.2023' #Snake case
# tomorrowDay = '10.02.2023' #Camel case

# num1 = 5
# num2 = 15
# result = num1 + num2
# print("Summa:", result)

# num1 = input('Enter number1:') # -> '5'
# num2 = input('Enter number2:') # -> '7'
# num1 = int(num1)
# num2 = int(num2)
# print(num2-num1)
# print (num2, '-', num1, '=', - num1)

# *
# num1 = int(input('Enter the num1:'))
# num2 = int(input('Enter the num2:'))
# print(num1, '*', num2, '=', num1 * num2)

# / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульное деление получение остатка от деления

# num1 = 7
# num2 = 3
# print('/', num1 / num2) (2.33335)
# print('//', num1 // num2)(2)
# print('%', num1 % num2)(1)

# ** -> возведение в степень 
# print (5 ** 2)
# print (16234 ** 53245)

# print(9 ** 0.5) квадратный корень числа

# pow - возведение в степень 
# pow(num1 , num2)
# num1= 5
# num2= 10
# print(num1 ** num2)

# print(pow(5, 10))

# print(5 ** 10)

# pow(num1, num2, <mod>)
# print(pow(5, 10 , 65))
# print (5 ** 10 %65)

# a=5
# b=2
# res = pow(a, b, 12)
# print(res)

## round () -  округление числа с плавающей точкой
# a = 5.36757
# print(round(a, 2))

# abs() - абсолютное значение числа -> abs(-5) -> 5
                                        #[-5] -> 5
# a = abs(-16)
# b = abs(15)
# print(a, b)

# divmod(a, b) -> Она выводит два числа , первое число это результат целочисленного деления (//) А на Вб а второе это модульное деление(%)
# res = divmod(5, 2) #(2, 1)
# print(res)
# print((5//2, 5%2))

# print(9 ** 0.5)

# import math 

# a = 5
# print(math.sqrt(a))

# a = 5
# print(round(math.sqrt(a),2))

# a= 5
# res = math.sqrt(a)
# print(round(res, 2))

#множественное присваивание 
#  оператор  присваивания (=)
# a = 5
# b = 15
# c = None

# c = a
# a = b 
# b = c

# print('a:',a, 'b:',b)

# c = a
# a = b 
# b = c
# a, b =b,a
#  #15, #5
# print('a:',a, 'b:',b)

# num1, num2 , num3 = input('num1:'), input('num2:'), input('num3')
# print(num1)
# print(num2)
# print(num3)

# '''Дана переменная с радиусом  окружности,найдите периметр и площадь окружности , результат выведите в терминал'''
# from math import pi

# r = int(input('VVedite radius:'))
# res_P = 2 * r * pi
# res_S = pi * (r ** 2)
# print('S оружности:', round(res_S, 2))
# print('P окружности:', round(res_P, 2))


# from random import randint

# print(randint(1, 10))

# name = input('Enter you name:')
# last_name = input('Enter your surname:')
# num = randint(1000000, 9999999)
# print(name, last_name, num)
# res = name + last_name + str(num)
# print(res)

# from random import randint

num = randint(1, 10)
i = 0

while i < 3:
    guess = int(input('Guess the number:') )   
    if guess == num:
     print('You won!Good job!')   
     break
    # i = i + 1 
    i += 1 #increment


temp = 65.5
res1 = (temp - 32) 
res2 = res1 * 0.5

print(round(res2, 2))













