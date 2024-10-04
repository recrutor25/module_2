#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 03 10 2024
@author: igor
"""
import random
def password(num):
    ps = []
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                ps.append(str(i) + str(j))
    return ps
num_1 = random.randint(3, 20)
result = password(num_1)
print(' Пароль: - число из первой вставки должно кратно','\n','делиться сумме '
      'значений цифр вводимого числа')
print('############# ', num_1, ' #############')
print(', '.join(result))

num_2 = input("###### Введите пароль:   ")
is_access = False
for i in range(0, len(result)):
    if result[i] == num_2:
        is_access = True
        print('Доступ разрешен')
        break
if not is_access:
    print('В доступе отказано')
