# Обработка исключений -> Try / except

# Errors -> связаны с кодом:
#     SyntaxError
#     IndentationError             Не воспроизводит код совсем!
#     TabError

# ИКЛЮЧЕНИЯ eexceptions -> связаны с данными которые передаются в код.

    # ZeroDivisionError
    # ArithmeticError
    # NameError                    Запускает код и выдает ошибку в том месте где произошла ошибка.
    # IndexError
    # KeyError
    # BaseException - прородитель всех исключений
# try:
#     a = int(input('Enter the number:'))
# except:
#     print('wrong data!')
# else:
#     print(a * 5)

# try:
#     <body>
# except:
#     <body> сработает если естьь ошибка
# else:
#     <body> если нет ошибки
# finally:
#     <body> сработает в любом случае

# ls = ['John', 'Snow', 'Tirion']
# try:
#     i = int(input('Vvedite index'))
#     print(ls[i])
# except (ValueError):
#     print('Вы ввели нерпавильные данные!')
# except (IndexError):
#     print('Вы ввели неправильный индекс!')

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Exception as e (error)
# dict_ = {'1': 'one', '2': ' two', 'name': 'John'}
# try:
#     key = input('Vvedite key: ')
#     print(dict_[key])
# except Exception as e:
#         print(f'Opps {e.__class__} error!')

# try:
#       num1 = int(input('Enter num1: '))
#       num2 = int(input('Enter num2: '))
#       result = num1 / num2
# except ValueError:
#       print('Invalid input!')
# except ZeroDivisionError:
#       print('Na 0 delit\' nel\'zya!')
# else:
#       print(result)
# finally:
#       print('The End!')
      
      




























































