# Create a program that reads any phrase and tells whether it is a palindrome, ignoring spaces. 

frase = str(input('Digite uma frase')).strip().upper()
palavras= frase.split()
junto = ''.join(palavras) #substitui os espaços por algo vazio ou pelo o que estiver das aspas
'''inverso = ''
for letra in range (len(junto) -1, -1, -1): #vai da ultima letra até a primeira
    inverso = inverso + junto[letra]'''
inverso = junto[::-1] #fatiamento que inverte a string
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('a frase digitada não é um palíndromo')