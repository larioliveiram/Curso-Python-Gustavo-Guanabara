# Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, display:
# A) How many times the value 9 appeared
# B) The position where the first 3 was entered
# C) Which numbers were even

tupla = (int(input('Digiteo valor 1: ')), 
int(input('Digiteo valor 2: ')), 
int(input('Digiteo valor 3: ')), 
int(input('Digiteo valor 4: ')))
print(f' A) {tupla.count(9)}')
print(f' B) {(tupla.index(min(tupla)))+1} posição')
print('C) Os números pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')