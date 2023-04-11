# найти квадрат и куб результат деления на 100 определенного числа:
# function ->  Функция это именнованая чатсь программы, которая содержит в себе определенный набор инструкций и может вызываться в других частях программы столько раз сколько угодно :)
# ->
# ->

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# DRY - don't repeat yourself
# num5 = 10
# print({'num':num5, '2': num5 ** 2,'3': num5 ** 3, '4': num5 / 100})
# num1 = 5
# num2 = 16
# num3 = 22
# num4 = 5830
# num5 = 24536
# num6 = 3456
# def operations(num):
#     print({'num':num, '2': num ** 2,'3': num ** 3, '4': num  / 100})
# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)
# operations(num6)

# def name_of_function(<a, b>) параметры :
    # <body> код, какая-то логиа , которая будет давать конечный результат
# <return> оператор который помогает вернуть результат

# name_of_func(5,6) (аргументы)

#параметры функуции - переменные которые будут принимать данные от пользователя и хранить в себе эти данные .

# аргументы функции - данные который мы передаем в фукнцию в моменте вызова.  

# print(len('str'))

# ls = [1,2,3,4,5]
# str1 = 'Hello world s vami Kani i Johnsnow!'
# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print(f'resul: {i}')

# our_len(ls)
# our_len(str1)

# def isEven(obj):
#     # if obj % 2 == 0:
#     #     return True
#     # else:
#     #     return False
    
#     return True if obj % 2 == 0 else False 

# print(isEven(5))
# print(result) # True
# print(isEven(5)) # False

# def is_even(num:int) -> bool:
#     """Our function returns True or False while checking number for even numeber"""
#     return True if num % 2 == 0 else False
# print(is_even(5))
# ----------------------------------------------------------------------------------------
# 2) Дан словарь а, значениями которого являются словари,
# измените словарь 'а' таким образом, чтобы значения внутреннего словаря стали 
# внешними значениями

# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

# Вывод:
# {'a': 32, 'b': 36, 'c': 37, 'd': 21}

# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# b = {}
# for k,v, in a.items():
#     b.setdefault(v,k)
# print(b)



# 3) Создайте словарь, где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
# a = {'apple':50, 'orange': 15, 'cherry': 51, 'banana': 70}
# for k,v in a.items():
#   if v % 2 == 0:
#     a.remove(k)
#   else:
#     print(k,v)

# try:
#     n = int(input('Введите число: '))
# except ValueError:
#     print('Неправильное значение!')
# else:
#     dict_ = {x: x** 2 for x in range(1,501) if x % n == 0}
#     print(dict_)

# 10 task comprehension 


# age = {'Murat': 24, 'Erzhan': 21, 'Karina': 24, 'Altynai': 17, 'Aybek': 16}
# for x in age:
#   if age[x] > 17:
#     print(f'{x} ne proshel')
#   else:
#     print(f'{x} ne proshel')


def add(num1: int or float, num2: int or float) -> int: 
  return num1 + num2
def subtract(num1 : int, num2: int) -> int or float:
  return num1 - num2
def multiply(num1 : int, num2: int) -> int or float:
  return num1 * num2
def division(num1 : int, num2: int) -> int or float:
  try:
      return num1 / num2
  except ZeroDivisionError:
      return 'На ноль делить нельзя!'

def calculate(num1,num2):
  operator = input('Введите оператор: (+ , - , / , *)')
  if operator == '+': return add(num1,num2)
  elif operator == '-': return subtract(num1,num2)
  elif operator == '/': return division(num1,num2)
  elif operator == '*': return multiply(num1,num2)
  else: return 'Вы ввели неправильный оператор'
  

def main():
  num1 = input('Введите число: ')
  num2 = input('Введите число: ')
  try:
    num1  = float(num1) if '.' in num1 else int(num1)
    num2  = float(num2) if '.' in num2 else int(num2)
  except ValueError:
    print('Вы ввели некоректное число!')
    main()
    return #try to remove this function

  while True:
    result = calculate(num1, num2)
    if type(result) == str:
      print(f'Результат: {result}')
    else: 
      print(f'Результат {result}')
      break
  
  question = input('Хотите продолжить?(Да/нет)').lower().strip()
  if question == 'Да': 
    main()
  else:
    print('Спасибо за использование нашего калькулятора!')

main()

  

















