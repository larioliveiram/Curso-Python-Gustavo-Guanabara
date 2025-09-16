# A teacher wants to randomly select one of their four students to erase the board. Write a program that helps them by reading the students' names and displaying the chosen one.

import random
a1 = input ('Qual o nome do aluno 1?')
a2 = input ('Qual o nome do aluno 2?')
a3 = input ('Qual o nome do aluno 3?')
a4 = input ('Qual o nome do aluno 4?')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno sorteado é o {escolhido}')