# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JhrQASyu_eYpoWXCmduN242PBfGe8kBX
"""

a=int(input("Enter first cost :"))
b=int(input("Enter second cost :"))
c=int(input("Enter third cost : "))
total_cost=a+b+c
if total_cost>50:
  total_cost=0.9*total_cost
print("The total cost :",total_cost)