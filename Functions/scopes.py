# Область видимости и пространство имен -(Scopes) 
# Технология которая определяет контекст имени(переменные) в рамках которого мы можем ее использовать.
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# built-ins(Втроенная область видемости) -> print, len, max, min,
# global(Глобальная) -> область одного файла \
# enlosed(не локальная, замкнутая) -> nonlocal
# local(локальная) -> облать внутри одной функции


# x = 200
# def my_func():
#     print(x)
#     a = 300
#     # print(a)

# my_func()
# print(x)

# a = 10 #global
# print() #built-in
# def hello(): #global
#     a = 'Hello wolrd' #local
#     print(a,'Local inside in func!')

# hello() 
# print(a,'global')

# LEGB - local enclosed global built-in - порядок поиска переменных в функции

# Enclosed
# Это замкнутое пространство имен - локальное пространство, у которого есть внутреннее (вложенное) пространство

# x = 'global'
# print(x,1)

# def enclosed(): #global
#     x = 'enclosed'
#     print(x)
#     def local(): # enclosed
#         x = 'local'
#         print(x,3)
#     print(x,2)
#     local()
#     print(x,4)

# enclosed()
# print(x,5)

# a = 5
# def func():
#     print(a)

# func()

# global -> позволяет изменять значения в глобальной переменной находясь внутри лоkальной области.

# nonlocal -> позволяет изменять значение не локальной (замкнутой) переменной находясь внутри локальной области

# var = 0

# def incrememnt():
#     global var
#     var += 1  #var = var +1

# print(var)
# incrememnt()
# print(var)

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter() #<function counter.<locals>.increment at 0x7f8dfd1480d0>
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())

# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# print(globals())
# globals - > функция которая возвращает все имена внутри глобальной области видимости

# locals - функции которая возвращает все имена внутри глобальной области видимости и локальной

def counter():
    num = 0
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

def showStats(heroes,mobs):
    print(f'JohnSnow ты убил:\n\tгероев: {heroes}\n\tмобов: {mobs} ')

counter_heroes = counter()
counter_mobs = counter()
heroes = 0
mobs = 0

print('Приветствую король севера John Snow в Вестеросе!')
while True:
    print()
    print('Тебе доступны следующие действия:')
    print('1-убить Героя, 2-убить моба, 3-статистика, 4-выйти из игры,')
    choice = input('Введите что хотите сделать: ').strip()
    if choice == '1':
        heroes = counter_heroes()
        print('Вы обезглавили Ланнистера!')
    elif choice == '2':
        mobs = counter_mobs()
        print('Вы убили белого ходака!')
    elif choice == '3':
        showStats(heroes,mobs)
    elif choice == '4':
        print('Пока пока! Ждем еще раз!')
        break
    
















































































