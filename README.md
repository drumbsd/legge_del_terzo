## Script dimostrazione Legge del Terzo

Questo script dimostra l'efficacia della legge del terzo. Applicato su un'ipotetica
estrazione di 90 numeri, dimostra che:

1. 1/3 circa dei numeri non viene estratto
2. 1/3 circa viene estratto 1 volta
3. 1/3 circa viene estratto piu' volte

Dopo la prima estrazione, se prendete la lista dei numeri non estratti, scoprirete che i 2/3 circa di questi
numeri verranno estratti nella successiva.

```
python main.py 

Numeri non estratti 31 Percentuale: 34 %
[1, 3, 5, 7, 8, 10, 15, 22, 24, 26, 29, 30, 32, 33, 34, 36, 37, 40, 42, 51, 54, 56, 58, 60, 61, 63, 68, 69, 82, 84, 85]

Numeri estratti 1 volta 34 Percentuale: 37 %
[2, 4, 9, 13, 16, 19, 21, 23, 25, 27, 31, 35, 38, 41, 43, 44, 47, 52, 53, 55, 62, 64, 65, 67, 70, 71, 74, 75, 76, 79, 81, 83, 86, 89]

Numeri estratti piu' volte 24 Percentuale: 26 %
[6, 11, 12, 14, 17, 18, 20, 28, 39, 45, 46, 48, 49, 50, 57, 59, 66, 72, 73, 77, 78, 80, 87, 88]
```

I seguenti numeri non sono stati estratti: 

`1,3,5,7,8,10,15,22,24,26,29,30,32,33,34,36,37,40,42,51,54,56,58,60,61,63,68,69,82,84,85`

Seconda estrazione

```
python main.py 

Numeri non estratti 34 Percentuale: 37 %
[3, 4, 6, 8, 10, 11, 12, 15, 21, 23, 26, 28, 31, 34, 35, 38, 44, 46, 47, 49, 51, 52, 56, 57, 58, 65, 67, 69, 71, 81, 82, 83, 85, 89]

Numeri estratti 1 volta 31 Percentuale: 34 %
[1, 2, 5, 9, 14, 16, 19, 22, 25, 29, 30, 36, 37, 40, 41, 42, 43, 45, 50, 54, 59, 64, 70, 72, 73, 74, 75, 76, 78, 80, 88]

Numeri estratti piu' volte 24 Percentuale: 26 %
[7, 13, 17, 18, 20, 24, 27, 32, 33, 39, 48, 53, 55, 60, 61, 62, 63, 66, 68, 77, 79, 84, 86, 87]
```

Dei precedenti 31 numeri non estratti, al ciclo successivo sono stati estratti:

`1,5,7,22,24,29,30,32,33,36,37,40,42,54,60,61,63,68,84` Per un totale di 19 numeri. I 2/3 di 31 e' pari a 20. 
