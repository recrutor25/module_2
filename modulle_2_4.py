#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30 09 2024
@author: igor
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
is_prime = True
# флаг позволяет пропустить 2 т.к. range(2,2) пробросит вложеный цикл
for i in numbers[1:]: # перебор списка начиная с двойки
    # перебор делителей
    for j in range(2, i):
        if i % j == 0 and i > 2:
            is_prime = False
            break
        else: is_prime = True

    if is_prime :
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)

