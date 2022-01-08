import matplotlib.pyplot as plt
import numpy as np
import random
from random import randint
from math import exp
T = 0.8 

on =[1,-1]
n = int(input('Введите число n>2 = '))
if n<=2: 
    n = 0; 
elif n < 2:  
     print('Error, please write n>2');
mas = np.ones((n,n))
for i in range(n):
    for j in range(n):
        mas [j,i] = on[randint(0,1)]
        
        
def summa(v):  #Сумма матрицы
    summ = 0
    mas00 = v.copy()
    for j in range(n):
        for k in range(n):
            if  j>=0: 
                summ += mas00[j,k] * mas00[j-1,k]
    for j in range(n):
        for k in range(n):
            if  k>=0: 
                summ += mas00[j,k] * mas00[j,k-1] 
    return(summ)


def ran(g): #Умнажает случайный элемент матрицы на -1
    mas_new = mas.copy()
    lol = np.arange(n)
    sl = lol[randint(0,n-1)]
    ko = lol[randint(0,n-1)]
    mas_new[sl,ko] = mas_new[sl,ko] * -1
    return (mas_new)


E1 = summa(mas)

for i in range (501):
    
    plt.imshow(mas)       
    
    mas2 = ran(1)
    E2 = summa(mas2)
    trig = E2 - E1
    
    if trig <= 0:  
        mas = mas2.copy()
        E1 = E2
        continue

    W = exp(-trig / T)
    P = random.random()
    while P == 0:
        P = random.random()
        
    if  P <= W:
        mas = mas2.copy()
        E1 = E2
        continue
    elif P > W:
         continue
print(mas)


