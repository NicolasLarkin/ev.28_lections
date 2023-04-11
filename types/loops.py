# i = 0
# while i > 10:
#     i += 1
#     print(f'Цикл сработал {i} раз')

# ls = list(range(1, 51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())

#----------------------------------------
# user = {'username': 'Johnsnow', 'password': 'ilovepython123'}
# i = 3
# password = None
# while password != input(f"{user['username']}vvedite parol\':") != user['password']:
#     # password = input(f"{user['username']}vvedite parol\':")
#     i -= 1
#     if i == 0 :
#         print('Vy zablokirovanny')
#         break
# else:
#     print(f"{user['username']} vy uspeshno zashli v sistemu!")


# input(f"{user['username']}vvedite parol\':")
#--------------------------------------------------------------------
# for <variable> in <iterable object>:
    # <body>

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_)
# print(i)
# print(next(i)) #0
# print(next(i)) #1
# print(next(i)) #2
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)) # stop itiration

# import random

# a = 1,2,3,4,5,6,7,8
# print(a)
# print(type(a))

# a,b,c = 1,2,3

# import random
# ls = []
# for x in range(1,101):
#     ls.append(random.randint(1,50))
# print(len(ls))
# ls = set(ls)
# ls = list(ls)
# print(ls)
# print(len(ls))

# ls = ['Tirion', 'Bilal', 'John', 'Sansa', 'Jamie', ' Eddart']
# for x in ls:
#     if x == 'Bilal':
#         continue
#     print(f'Hello Mr/Mrs {x}!')

# i = 0
# while i < 100 :
#     i += 1
#     if i%2 == 0:
#         continue
#     print(i)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# число 100 
# # 1,2,4,5,10,20,25,50,100
# num = 1_000_000_000_000_000
# res = []

# for x in range(1,int(num ** 0.5) +1):
#     if num % x == 0:
#         res.extend({x, num // x })
# res.sort()
# print(res)








# age = {'Murat': 24, 'Erzhan': 21, 'Karina': 24, 'Altynai': 17, 'Aybek': 16}
# forbidden = []
# accessed  = []
# for k, v in age:
#     if  v > 17:
#         forbidden.append(v)
#     else:
#         accessed.append(v)
# print(len(forbidden))
# print(len(accessed))




# while True:
#   money = float(input('Введите сумму денег в вашем кошельке:'))
#   if money == 0:
#    print('Сумма не может быть отрицательной! Введите еще раз!')
#   else:
#    print('Браттаан, да ты богат :)')


# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sort= dict_.sort
# print(sort)





































































