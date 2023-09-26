# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:13:41 2023

@author: jules
"""
import pandas as pd

def func1():
    print("meth1")

def func2(arg1):
    print("meth2")
    print(arg1)

print(func1())

print(func2("Jules"))


df= pd.read_csv('pokemon.csv')

print(df["Name"])

print(df.columns)


for r, rij in df.iterrows():
    print(rij["Name"])

