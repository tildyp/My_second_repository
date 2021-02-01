# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Adjon meg egy egész számot")
n = int(input());
n_list = [i for i in range(2,n)]

n_vizsg=int(n**0.5);

for ii in range(2, n_vizsg+1):
    for jj in n_list:
        if jj%ii==0 and jj>ii:
            n_list.remove(jj)
    
