# words = ['John', 'Ono', 'kazak' ,'peter', 'radar', 'apa', 'dovod']
# def get_polindrom(words):
#     res = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             res.append(word)
#     return res
# polindrom_words = get_polindrom(words)
# print(polindrom_words)

# def mahinacii(money,period):
#     if money < 30000:
#         raise ValueError('Вложить можно более 30000')
#     if period < 3:
#         raise ValueError('Период должен быть не менее 3х лет')
#     year = 0

#     while year < period:
#         money += money * 0.1
#         year += 1
#     return money
# try:
#     money = float(input('Введите сумму вложения: '))
#     period = int(input('Введите период: '))
#     print(mahinacii(money,period))
# except ValueError:
#     print('Неправильный ввод!')

# def test_func(a=1,b=4):
#     pass
# test_func()

# def range(first,last,step = 1):
#     pass
# range(stop = 5,start = 3,step = 2)

