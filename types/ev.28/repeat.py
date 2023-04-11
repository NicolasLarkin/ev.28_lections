# from random import randint
# ls = []
# for x in range(0, 100):
#     ls.append(randint(0,100))

# ls.sort()
# print(ls,len(ls))


# res = []
# for x in ls:
#     if x not in res:
#         res.append(x)
# print(len(res))


# x1 = int(input('Vvedite 1 coordinatu gde stoit ladya;'))
# y1 = int(input('Vvedite 2 coordinatu gde stoit ladya'))
# ladya = [x1, y1]
# x2 = int(input('Vvedite 1 coordinatu gde stoit ladya;'))
# y2 = int(input('Vvedite 2 coordinatu gde stoit ladya'))
# target = [x2, y2]

# if x1 == x2 or y1 ==y2:
#     print(True)
# else:
#     print(False)

# ------------------------------------------------------------------__----------------___########################
# import random
# ls = ['plov', 'bsh-barmak', 'kurdak', 'oromo', 'lagman']
# p = 0
# b = 0
# k = 0
# o = 0
# l = 0

# for x in range(0, 1000000):
#     meal = random.choice(ls)
#     if meal.lower()== 'plov':
#         p+= 1
#     elif meal.lower() == 'kurdak':
#         k += 1
#     elif meal.lower() == 'bsh-barmak':
#         b += 1
#     elif meal.lower() == 'oromo':
#         o += 1
#     else:
#         l+= 1

# print('Результаты Голодных игр:')
# print(f'Plov:{p}, \nbsh-barmak:{b}\nkurdak:{k}\noromo:{o}\nlagman:{l}')

#-------------------------------------------------------------------------------------
#Given an array of integers nums and an onteger target, return indices of the two numberssuch that they add upp to target

#1) nums = [2,7,11,15]
#target = 9
#0,1 -----------------2+7 =9

#nums = [4,11,2,5,1,6]
#target = 8
# 2, 5 ---------------- 2+6=8


# nums = [2,7, 11, 15]
# target = 9

# for i in range (0,len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         print(f'Otvet:{i},{nums.index(num)}')
#         break

# nums = [4,11,2,5,1,6]
# target = 8

# for i in range (0,len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num != nums[i]:
#          print(f'Otvet:{i},{nums.index(num)}')
#          break
















