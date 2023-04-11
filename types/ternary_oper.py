# sentence = input('Vveditepredlojeniye:')
# if sentence[-1] == '?':
#     print('Yes voprositelnoe!')
# else: 
#     print('No normal one1')


# print('Yes voprositelnoe!' if sentence[-1] == '?' else 'No normal one!')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Ternary operators(Тернарный оператор) - это конструкция которая по своему действию аналогична конструкции if/else, но при этом записывается в одну строчку
# while True:
#     number = int(input('Введите число :'))
#     res = 'even number' if number % 2 == 0 else 'odd number'
#     print(res)

# <выражение если True> if <условие> else <выражение если False>

# ls =[55,65, 75 ,89, 100 , 15 , 6]
# print(ls)
# choice = input('Vvedite max/min :')
# # res = max(ls) if choice.lower().strip() == 'max' else min(ls) #
# # print(res)
# if choice.lower().strip() == 'min':
#     print(min(ls))
# elif choice.lower().strip() == 'max':
#     print(max(ls))
# else:
#     print('Invalid choice!')
#-----------------------------------------------------------------------------------------
# flag = True
# symbols = '0123456789'+'-'+'.'
# while flag: 
#     num1 = input('Введите первое число: ')
#     is_correct_number = True
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели неправилное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#             continue

#     num2 = input('Введите второе число:')
#     for x in num2:
#         if x not in symbols:
#             print('Вы ввели неправилное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue
    
#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)


#     operator = input('Введите оператор(+, -, *, .):')

#     if operator == '+':
#         print(f'Резульлтат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Резульлтат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Резульлтат: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результат: {num1 / num2}')

#     else:
#         print('Вы ввели неверный оператор!')

#     choice = input('Хотите продолжить (Да/Нет)?')
#     if choice.lower().strip() != 'да':
#         flag = False
#         print('Спасибо что были с нами!')
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(x * y)
if x % y == 0:
    print(f'{x} делится на {y} без остатка! ')
    print(x % y)
else:
    print(f'{x} не делится на {y} без остатка! ')
    print('Частное:')
    print(x / y)
    print('Остаток:')
    print(x % y)





































