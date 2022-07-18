import random
import pandas as pd
import numpy as np
import os

a = []
for i in range(10):
    num = round(random.uniform(1000000000,9999999999))
    a.append(num)
    for i in range(19):
        blank = ''
        a.append(blank)

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

