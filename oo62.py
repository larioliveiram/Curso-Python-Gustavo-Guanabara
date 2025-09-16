# Improve Challenge 61 by asking the user if they want to display more terms. The program will end when the user chooses to display 0 terms.

a = int(input('Digite o primeiro número:'))
r = int(input('Digite a razão: '))
c = 0
while c <= 10:
     print( f' {a + r*c} >  ' if c<10 else f'{a + r*c}.', end=' ')
     c+=1
while True:
     print()
     resposta = str(input('Quer mais algum termo? ')).strip().upper()
     if resposta in ['SIM', 'S', 'SI']:
          termo2 = int(input('Quantos termos você quer mostrar a mais?'))
          c2 = c
          while c2 < c + termo2:
               print (f'  {a + r*c2} ', end=' ')
               c2+=1
          c = c2
     elif resposta in ['NÃO', 'N', 'NAO']:
           print('Esta é a sua PA finalizada.')
     else:
          print('Resposta inválida. Por favor, responda com SIM ou NÃO.')



