from random import *
from termcolor import colored

counter = 0
counter1 = 0
countermolti = 0
nonestratti = []
estrattiunavolta = []
estrattipiuvolte = []
tabella = dict.fromkeys(range(1,91),0)
for i in range (1,91):
    numero = randint(1,91)
    tabella[numero] += 1
for i in range (1,91):
    if tabella[i] == 0:
       counter += 1
       nonestratti.append(i)
    elif tabella[i] == 1:
        counter1 += 1
        estrattiunavolta.append(i)
    elif tabella[i] > 1:
        countermolti += 1
        estrattipiuvolte.append(i)
print()
print("Numeri non estratti",len(nonestratti), "Percentuale:", colored(int(len(nonestratti)*100/90),"red"),"%")
print(nonestratti)
print()
print("Numeri estratti 1 volta",len(estrattiunavolta), "Percentuale:", colored(int(len(estrattiunavolta)*100/90),"red"),"%")
print(estrattiunavolta)
print()
print("Numeri estratti piu' volte",len(estrattipiuvolte), "Percentuale:", colored(int(len(estrattipiuvolte)*100/90),"red"),"%")
print(estrattipiuvolte)
