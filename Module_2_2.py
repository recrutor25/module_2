#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 09 2024
@author: igor
"""
first = int(input('введите первое число:   '))
second = int(input('введите второе число:   '))
third = int(input('введите третье число:   '))

if first == second and first == third and second == third:
    print('3') # если равны все числа
elif first == second or first == third or second == third:
    print('2') # если равны любые два числа
else:
    print('0') # иначе числа не равны



