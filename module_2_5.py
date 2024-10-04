#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 02 10 2024
@author: igor
"""
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)  # Пишем в список значение
    print(matrix)
result1 = get_matrix(2, 2,10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

