# class Class1:

#     def first(self):
#         pass

#     def second(self):
#         pass

# class Class2(Class1):

#     def third(self):
#         pass

#     def fourth(self):
#         pass

# obj = Class2(Class1)
# obj.first
# obj.second
#----------------------------------------------------
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()
#------------------------------------------------------
class MyString(str): 
    def __init__(self, stroka1): 
        self.stroka1 = stroka1 
        
    def append(self, stroka2): 
        self.stroka2 = stroka2 
        self.stroka1 = self.stroka1 + self.stroka2 
        return self.stroka1 

    def pop(self): 
        last_w = self.stroka1[-1] 
        self.stroka1 = self.stroka1[:-1] 
        return last_w 
    
    def __str__(self) -> str: 
        return self.stroka1 
    
example = MyString('String') 
example.append('hello') 
print(example.pop()) 
print(example)