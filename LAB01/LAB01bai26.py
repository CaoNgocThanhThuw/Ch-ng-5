# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:43:52 2024

@author: Cao Ngọc Thanh Thu 23719291
"""
# phần a
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
solon = max(a,b,c)
sonho = min(a,b,c)
d = a + b + c - solon - sonho
print("Số xếp theo thứ tự tăng dần:",sonho,",",d,",",solon)
# phần b
a=int(input("Nhập số thứ nhất: "))
b=int(input("Nhập số thứ hai: "))
c=int(input("Nhập số thứ ba: "))
d=int(input("Nhập số thứ tư: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if a > d:
    a, d = d, a
if b > c:
    b, c = c, b
if b > d:
    b, d = d, b
if c > d:
    c, d = d, c
print("Số xếp theo thứ tự tăng dần: ", a, b, c, d, sep = "")