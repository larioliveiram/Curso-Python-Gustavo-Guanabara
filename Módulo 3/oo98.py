# Create a program with a function called counter(), which receives three parameters: start, end, and step, and performs the counting. Your program must carry out three counts using the function:
# A) From 1 to 10, counting by 1
# B) From 10 down to 0, counting by 2
# C) A customized count

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo == 1
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    sleep(1)
    if inicio < fim:
        for n in range(inicio, fim+1, passo):
            print(n, end=' ')
    else: 
        for n in range(inicio, fim-1, -passo):
            print(n, end=' ')
    print()
    print('-='*30)

contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem') 
inicio = int(input('inicio:'))
fim = int(input('fim:'))
passo = int(input('inicio:'))
contador(inicio, fim, passo)