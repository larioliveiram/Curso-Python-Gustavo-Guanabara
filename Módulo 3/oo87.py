# Improve the previous challenge by showing, at the end:
# a) The sum of all even values entered
# b) The sum of the values in the third column
# c) The largest value in the second row

lista = list()
for c in range (0,9):
    n = int(input('Digite um número: '))
    lista.append(n)
par = 0
for n in lista:
    if n % 2 == 0:
        par += n
print(f'| {lista[0]} | {lista[1]} | {lista[2]} |')
print(f'| {lista[3]} | {lista[4]} | {lista[5]} |')
print(f'| {lista[6]} | {lista[7]} | {lista[8]} |')
print(f' A soma dos valores pares da {par}')
print (f' A soma dos valores da terceira coluna da {lista[2]+lista[5]+lista[8]}')
linha2 = (lista[3], lista[4], lista[5])
print(f' O maior valor da segunda linha é {max(linha2)}')
