# Write a program that reads a phrase from the keyboard and displays:
# 1. How many times the letter "A" appears
# 2. The position where it first appears
# 3. The position where it last appears

frase = input('Digite uma frase').strip().upper()
print(f' NA frase tem {frase.count('A')} letras A')
print(f' Sendo que o primeiro aparece na posição {frase.find('A')} \n e o último na posição {frase.rfind('A')}')

# o .rfind ele vai começar a contar a partir do final


