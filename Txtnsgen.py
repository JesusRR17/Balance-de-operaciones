import random
import pandas as pd
import numpy as np
import os

num = random.sample(range(1000000000,9999999999),10)

a = []
for i in range(10):
    num_temp = num[i]
    a.append(num_temp)
    for i in range(19):
        a.append(num_temp)

b= []
for i in range(200):
    c = str(round(random.uniform(-2000.00, 2000.00),2))
    c ='$' + c
    b.append(c)

d = []
for i in range (200):
    e = '¿?'
    d.append(e)

TXNsdf = pd.DataFrame(list(zip(a,d,b)))

if os.path.isfile("TXNs.txt"):
    os.remove("TXNs.txt")
TXNsdf.to_csv('TXNs.txt', header=None, sep=' ', index=None, mode='a', encoding= 'utf-8')

