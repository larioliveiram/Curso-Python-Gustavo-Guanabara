# Develop a program that reads the lengths of three line segments and tells the user whether they can form a triangle or not.


a = float(input('Qual o comprimento da primeira reta?'))
b = float(input('Qual o comprimento da segudna reta?'))
c = float(input('Qual o comprimentod a terceira reta?'))
if a+b>c and a+c>b and b+c>a:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')