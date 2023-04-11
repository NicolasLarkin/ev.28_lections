# def my_decorator(func):
#     def wrapper():
#         print("До вызова функции")
#         func()
#         print("После вызова функции")
#     return wrapper

# @my_decorator
# def my_function():
#     print("Привет, я функция!")

# my_function()

# a1 = {1:30,2:10,12:90}
# a2 = dict(b=20,c=29,d=56)
# a3 = {}
# for k,v in a1.items():
#     a3.setdefault(k,v)
# print(a1,a2,a3)


# a1 = {1:30,2:10,12:90}
# print(type(a1))

string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_ = [value.split() for value in string_.values()]
print(list_)