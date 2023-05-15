import random
ls = ['Plov', 'Besh', 'Kuurdak', 'Oromo', 'Lagman']
p = 0
b = 0
k = 0
o = 0
l = 0

for x in range(0, 100000):
    meal = random.choice(ls)
    # print(meal)
    if meal.lower() == 'plov':
        p += 1
    elif meal.lower() == 'besh':
        b += 1
    elif meal.lower() == 'kuurdak':
        k += 1
    elif meal.lower() == 'oromo':
        o += 1
    elif meal.lower() == 'lagman':
        l += 1
    else:
        l += 1

print('Результаты голодных игр:')
print(f'Plov: {p}\nBesh: {b}\nKuurdak: {k}\nOromo: {o}\nLagman: {l}')

dict_ = {'Plov':p, 'Besh-barmak': b, 'Kuurdak': k, 'Oromo': o, 'Lagman': l}
print(dict_)
res = sorted(dict_.items(), key=lambda x: x[1], reverse=True)[0]
print(f'Победило блюдо {res[0]} и оно набрало: {res[1]} очков!')


