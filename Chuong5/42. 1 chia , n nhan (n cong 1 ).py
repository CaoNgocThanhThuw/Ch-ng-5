# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:43:51 2024

@author: Admin
"""

n = int(input("Nhập giá trị n: "))
s = 0

for i in range(1, n+1):
  s += 1 / (i * (i+1))

print("Tổng S(n) =", s)