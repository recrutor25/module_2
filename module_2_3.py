#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30 09 2024
@author: igor
"""
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
while n < len(my_list):
    if my_list[n] > 0:
        print(my_list[n])
    elif my_list[n] == 0:
        n += 1
        continue
    else:
        break
    n += 1

