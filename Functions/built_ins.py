# zip(iterables) - она соединяет каждый элемент итерируемых обьектво ммежду собой в тип данных tuple и возвращает итератор.

# ls1 = [1,2,3]
# ls2 = [100, 200, 300]
# result = dict(zip(ls1,ls2))
# print(result)

# ls1 = [1,2,3,4,5]
# ls2 = [100, 200, 300,400,500,600]
# ls3 = [10, 20, 30]

# result = list(zip(ls1,ls2,ls3))
# print(result)

# zip для создания словарей 

# d_keys = ['hostname', 'location','vendor', 'model', 'IP']
# data = {
#     'oktbr':['bishkek_oktbr','Gorkaya 212', 'Vefa', 'Cisco','10.244.0.12'],
#     '1may':['bishkek_1may','Gorkaya 252', 'Cum', 'MI','15.344.0.12'],
#     'chui':['bishkek_chui','Flash 234', 'Gum', 'UTy','10.098.0.12']
# }
# bishkek_data = {}
# for k in data:
#     bishkek_data[k] = dict(zip(d_keys,data[k]))

# print(bishkek_data)

#----------------------------------------------------------------------------------
# all(),any()
#all(itrable) - Возвращает True, если все элементы итерируемого объекта истина, иначе False

# ls = [5,6,7, []]
# print(all(ls)) # True

# ip = '10.255.0.155' # True
# ip1 = '10.125.0y.202' #False

# result = all( x.isdigit() for x in ip1.split('.'))
# print(result)

#any(iterable) - Возвращает False, если хотя бы один элемент истина.

# ls = [1,3, [1,2] , 0]
# print(any(ls))

# ignore = ['rm-rf', 'sudo','reset','poweroff']
# command = input('Введите команду: ')
# if any(x in command for x in ignore):
#     raise Exception('Block You!')
# print('It\'s okey')

#-----------------------------------------------------------------------
# from random import choices
# from string import ascii_letters, digits,punctuation
# from itertools import repeat 

# symbols = '_()+-@!3$'
# q_pass = int(input('Введите количество паролей: '))
# result =  {
#     f(choices(ascii_letters,k=15), choices(digits, k =6), choices(symbols,k=2))
#     for f in repeat(lambda x,y,z: ''.join(set(x+y+z)),q_pass)


# }

# print(result)
# print(f'Quantity of passwords: {len(result)}')

# from statistics import mean
# print(f'Средняя длина паролей: {mean(len(x) for x in result)}')

# num = [3]
# def mul(square):
#   ans = square ** 2
#   num.append(ans)
# mul(4)
# print(num)

# def amount(x,y):
#   x = input('Введите слово:')
  


# list_ = [1,2,3,4]
# result = [x**2 for x in list_]
# print(result)

num = [3]
def mul(square):
  ans = square ** 2
  num.append(ans)
mul(4)
mul(5)
mul(8)
print(num)













































