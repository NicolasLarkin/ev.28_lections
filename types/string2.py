# print(dir(str))
# print(dir(int))

# a = 'Hello'
# b = 'John'
# # print(a != b)
# # print('abc' == 'abc')
# print(a > b)
# print(a < b)

# print('a') # 97 -> 1100001
# print('a' > 'b')
# print('h' > 'c')

# print('hello' > 'harry') 
# print('abc' > 'abc')

# len() - возвращает количество символов в строке
# a = 'johnsnow'
# b = 'Hello'
# print(len(a) > len(b))
# print(len(a), len(b))

# # > < == != >= <=

# Методы строк
# replace(old, new, [count]) - меняет  в строке символы old на new если вы укажете cout то заменит count еще раз

# text = 'ha ha ha ha'
# result = text.replace('a' ,'e', 2)
# print(text) 
# print(f'result after replace: {result}')

# str1 = 'hello world! My name is John Snow!'
# res = str1.replace('John Snow' , 'Tirion Lannister')
# print(res)

#strip() - Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))

# print(dir(str))

# isdigit - ->     Проверяют 
# isnumeric - -> состоит ли наша строка полностью
# isdecimal - -> из чисел

# num = input('Vvedite chislo:')
# print(f'Vvedeno chislo?: {num.isdigit()}')

# num = input('Vvedite chislo:')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5 }')
# else:
#     print(f'Vy vveli ne chisla!')

# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())

# isalnum()-> проверяет состоит ли наша строка из чисел и символов латинского алфавита и кириллицы

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha () -->  состоит ли наша строка полностью из символов алфавита

# text = "Hello world"
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())

# islower()
# isupper()
# istitle()
# str1 = 'Is'
# print(str1.islower()) #is
# print(str1.isupper()) #IS
# print(str1.istitle()) # Is


# index(value , [start] , [end]) - выводит индекс значения value которое мы передаем в нашей строке.

# text = 'Hello john snow'
# print(text.index('john', 2 , 5))

# text = "Hello world! My nome is John Snow!" #o
# # print(text.index('John'))#
# res = text.index('o')
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)

# count(value, [start]) - считает кол-во вхождений value в нашу строку

# text = 'hello o o o hello'
# print(text.count('o'))
# print(text.count('hello'))

# split(separator) - дробит нашу строку на несколько частей по разделителю , все части строк сохраняются в типе данных list


# text = 'Let me speak, by my heart on English! Cause my name is Gulchapchap'
# res = text.split(' ')
# print(len(res))

# a = '#hello#hello#hello#hello'
# res = a[1:].split('#')
# print(res)

# 'connector'.join(lest) -> соединяет по  connector строки которые находились в list
# text = 'Let me speak, by my heart on English! Cause my name is Gulchapchap'
# res = text.split(' ')
# print(res)
# str1 = '_'.join(res)
# print(str1)

# find(value, [start], [end]) -> делает тоже самое что и index, но если не нашел то вернется -1. 

# text = 'hello'
# print(text.find('l'))
# print(text.find('lytui'), type(text.find('lytui')))
# print('John Snow')

# swapcase() - переводит все символы в противоположный регистр
# upper() -переводит все в верхний регистр 
# lower() - переводит все в нижний

# text = 'Hello World, JOHN snow'
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() -> переводит самый первый символ в верхний регистр
# tittle() -> он переводит первые символы всех слов в верхнйи регистр

# name = input('Vvedite imya:').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'john edart snow'
# print(fio.title())

# print(dir(str))



set()





















