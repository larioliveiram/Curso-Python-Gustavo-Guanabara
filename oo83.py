# Create a program where the user enters any expression using parentheses. Your application should check whether the expression has the parentheses opened and closed in the correct order and quantity.


frase = str(input('Digite uma expressão:'))
lista = []
for p in frase:
    if p == '(':
        lista.append(1) #adiciona na lista x
    elif p == ')':
        if len(lista) > 0:
            lista.remove(1) # se já tem o ( na lista, tira da lista de fica "par"
        else:
            lista.append(1) # se não tinha (, adiciona na lista o fechamento, sinalizando que tem a mais
            break
if len(lista) == 0: 
    print('Sua expressão é válida')
else: # se tem 1 parentese sobrando na lista, errado
    print('Sua expressão está errada!')