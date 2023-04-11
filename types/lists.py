# list() - (списки, массив) - изменяемый, последовательный тип данных, который представляет с собой коллекцию каких либо объектов (значения).

# my_list = [1, 'string', False, None, [1,2,3,4,5]]
# print(my_list, type(my_list))

# # range() - возвращает последовательность  элементов(чисел)
# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)

#list
# my_list = list('Hello WOrld')
# print(my_list)

# tuple_ = ('banana', 'applle', 'cherry')
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls, type(ls))

# Индексация в списках 
# ls = [1,2,3,4,5, 'String', [True, False, None]]
# print(ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:])

# ls = [1,2,3,4,5, 'String', [True, False, None]]
# print(ls[6])#True

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# ls = list(range(1, 11))
# print(ls)
# for num in ls:
#     print('Hello')

# ls = ['John', 'Sansa', 'tirion', 'Jamie']
# print(len(ls))
# for x in ls:
#     print(f'Hello mr/mrs {x}! Welcome to the club!')

# ls -> 1 , 21 четных чисел - квадрат числа, нечетынх чисел куб

# ls = list(range(1,21))
# print(ls)
# for num in ls:
#     if num % 2 == 0:
#         print(f'Число четное {num}, квадрат:{num**2} ')
#     else:
#         print(f'Число нечетное {num}, куб: {num**3}')

 #---------------------------------------------------------------------------------------------------------------------------------------------------------
# Методы списков
# print(dir([]))
# append(element)- Добавляет элемент в конец списка 

# ls = [1,2,3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello')
# ls.append([1,2,3,4])
# print(ls,len(ls))

#extend(object) -  расширяет список
# ls =[1,2,3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# ls.extend(str(56))
# ls.extend([1,2,3])
# print(ls)

# ls = [1,2,3]
# ls1 = [4,5,6]
# print(ls + ls1)

# sort() - сортирует список если передать reverse = True, то список отсортируетяс в убывающем порядке

# from random import randint
# ls = []
# for x in range(0,100):
#     num = randint(0,1000)
#     ls.append(num)

# print(ls)
# ls.sort(reverse=True)# Перевернуть список
# print('After')
# print(ls)

# ls = ['John', 'Deyneris', 'Tiion', ' Aizirek']
# ls.sort(key=len, reverse=True)
# print(ls)

# insert(index, element) - добавляет элемент по указанному index(у)

# ls = ['String', 2,3 , False]
# ls.insert(0, [1,2,3])
# print(ls)

# remove(element),[start], [end] - удаляет элемент из списка, если такого нет то выводится ошибка.
# pop([index]) - удаляет и возвращает элемент из списка по index, который мы передаем, но если index не передать то удаляет последний элемент

# ls = [5,1,2,4,4,5,5,5]
# # ls.remove(5)
# # print(ls)
# # print(5 in ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)

# ls = [5,1,2,4,5,5]
# print(ls.pop(0))#5
# print(ls.remove(5))#None
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update --------------
# ls = [1,'h', 3]
# print(ls)
# ls[1]= 2
# print(ls)
# print(ls.reverse())
# print(ls)
# print(ls[::-1])

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if x.startswith('f'):
#         spisok.append(x)

# print(spisok)

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)

# print(spisok)























































































































