# first_size = 100

# def second():
#     second_size = 50
#     global first_size
#     first_size += second_size
#     def third():
#         third_size = 25
#         global first_size
#         first_size += third_size
#     third()

# second()
# print(first_size)

# l1s = ['hello', 'word', 'min']
# ls = [1,2,3,4,5,6]
# new_list = list(map(lambda x: x** 2 if x % 2 == 0 else x, ls))
# print(new_list)

# new_ls = max(ls,key=len)
# print(new_ls)

# new_list = list(map(len,ls))
# print(new_list)

# new_list = list(filter(lambda x: len(x) > 4,ls))
# print(new_list)

# sogl = 'бвгджзклмнпрстфхцчшщ'
# glas = 'эеёиоуэюя'
# def let_count(word:str):
#     res_sogl = 0
#     res_glas = 0
#     res_another = 0 
#     for letter in word:
#         if letter in sogl:
#             res_sogl += 1
#         elif letter in glas:
#             res_glas += 1
#         else:
#             res_another += 1
#     return res_sogl, res_glas, res_another
# a = let_count('привет')
# print(a)

# names = ['Tom', 'John Snow', 'Rachel', 'Sam', 'Sanzhar']
# new_names = ['short' if len(x) <= 3 else 'long' for x in names]
# print(new_names)

# def separateDigits(self, nums):
#     res = []
#     for i in nums:
#         ls = list(map(int,str(i)))
#         print(ls)
#         res.extend(map(int,str(i)))
#     return res

# def maximumCount(self, nums):
#     pos = 0 
#     neg = 0
#     for i in nums:
#         if i > 0:
#             pos += 1
#         elif i < 0 :
#             neg += 1
#     return max(pos,neg)
     

# maximumCount()


def func(arg, arg1 = 1):
    print(arg,arg1)

func(arg1 = 2, arg = 1)





































