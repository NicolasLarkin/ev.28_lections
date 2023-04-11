# Операторы сравнения 
# Условные операторы и логические операторы

# операторы сравнения
# <, >, ==(равно) , != (не равно) , <=, >=

# 1 < 5-> True
# 7 > 9-> False

# ord('h') - ascii code review
# chr(number) -> symbol 

# Условные операторы 
# if
# elif
# else

# if<condition>
#     <body if> #сработает если в condition if придет true
# [elif] <condition>
#     <body elif>
# [else] :
#     <body else>#срабоатет если во всех выше стоящих условиях пришло false

# string = input('Enter something:')

# if string.lower() == 'hello':
#     print('Hello it\'s me i was wondering if after all these years you\'d like to meet')
# elif string.lower() == 'john':
#     print('welcome back John Snow, king of the North!')
# elif string.lower() == 'abra-kadabra':
#     print('Sim salamon Wooduo')
# else:
#     print('Nothing can ever heal me!')

# print('Registration form:')
# email = input('Enter you email:')
# password = input('Enter the password:')
# if len(password) < 8: #
#     raise ValueError('Pasword is too short!\nNeed to be 8 symbols or more!')
# elif password.isdigit():
#     raise ValueError('Password must contain numbers or special sybmols too')
# elif password.isalpha():
#     raise ValueError('Password must contain numbers too!')

# password2 = input('Enter password confirmation:')

# if password != password2:

#     raise ValueError('Passwords did not match!')

# print(f'Succesfully registered! Hello mr/mrs {email}!')

# age = input('Enter your age:')

# if age.isdigit():
#     age = int(age) 
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access denied! Come again after {18-age} years')
# else:
#     print('You can pass! Welcome to KZ!')


# and 
# or лог или 
# not лог отрицание

# money = 1_000_001
# status = 'premium'

# if money > 1_000_000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money < 1_000_000  or status == 'premium':
#     print('You\'re ministr of our club!')
# else: 
#     print('You\'re  a honorable member of our club!')

# str1 = 'Hello world'
# print(str1)
# symbol = input('Enter the symbol:')

# if symbol not in str1:
#     print(f'The symbol: \'{symbol}\' does not exists!')
# else:
#     print(f'The symbol:{symbol} exists!')

# if symbol  in str1:
#      print(f'The symbol:{symbol} exists!')
# else:
#      print(f'The symbol: \'{symbol}\' does not exists!')

# Разрешаем доступ если он юзер гита или гугла и его возраст больше 21 и у него деньги(10000)

# user = 'John'
# is_google_user = True
# is_github_user = False
# age = 19
# user_coins = 11000

# if (is_github_user or is_google_user) and (age > 21 or user_coins > 10000):
#     print(f"You can enter the system:) mr/mrs{user}")
# else:
#     print('Sorry, you couldn\'t enter! ')
