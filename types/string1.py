# 'String - строки'
# "Hello world true 5 None"

# """ 
# Hello World
# My name is John Snow
# """


# Строки - набор последовательных символов , которые мы используем для хранения и представления текстовой информации


# Индексация в строке 
# name = 'John'
        # j = 0 = -4
        # o = 1 = -3 
        # h = 2 = -2
        # n = 3 = -1
# print(name)
# print(name[0])
# print('kani'[-1], 'kani'[0])

# str1 = 'birthday'
# print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4] )

# print(str1[5]+ str1[6]+  str1[7])

# Срезы - по индексам
# [start: end; <step>]

# str1 = 'birthday'

# print(str1[5:] )
# print(str1[:5])

# text = 'HelloWorld! My namae is John i\'m the King of the North'
# print(text[:13])  
# print(text[::2])

# print(text[::-1])


#  Конкетенация строк(соединение)

# a = 'Hello'
# b = 'World'
# c = " "
# print(a+c+b)

# Экранирование - способ записи символов в строку, которые невозможно ввести с клавиутуры

#  \n -> перенос строки 
# \t -> горизантальная табуляция
# \v -> вертикальная табуляция
# \f -> перевод страницы
# \r -> возврат указателя
# print('\vHello \tWorld!\n My name is Johnsnow!')

# Форматирование строк
# 1 с помощью %
# 2  с использованием .format()
# 3 ИНерполяция строк (преобразование, f-stroki)


# %
# name = input('Vvedite imya:')
# last_name = input('vedite last_name:')
# # print('Добро пожаловать к нам ' +'name' +"" + last_name + "!") 1-вариант

# print('Hello mr/mrs %s %s!' %(name, last_name)) #2 -  вариант 

# .format
# name = input('Vvedite imya:')
# # last_name = input('vedite last_name:')
# # print('Приветствую вас,{} {}, в наш клуб!'.format(name, last_name)) 


# #f-stroki

# # a = input('Enter mr/mrs:')
# # name = input('Vvedite imya:')
# # last_name = input('vedite last_name:')
# # print(f'Hello {a}{name} {last_name}! Welcome to the party!')

# text = 'Запомни Питтер, с большой силой приходит и большая ответственность.'
# reversed_text = text[::-1]
# print(reversed_text)
# len_text = len(reversed_text)
# i = 0
# count_t = 0
# print(len(reversed_text))
# while i < len_text:
#         symbol = reversed_text[i]
#         if symbol == 'т' or symbol == 'Т':
#                 count_t += 1
#         # print(symbol)
#         i+= 1 #инкремент  i = i + 1

# print(f"В тексте буква 'т' встретилась {count_t} раз! ") 

# decimal = 10
# print(decimal ** 3)
# print(decimal ** 3)
# print(decimal * 0.5)

# y = 3
# print(y ** 2)
# yanswer = print(y ** 2)
# print(yanswer % 5)



# task 12 PY
# decimal = 4.0
# print(decimal ** 2)
# print(decimal ** 3)
# print(decimal * 0.5)




 




























































