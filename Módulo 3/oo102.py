# Crie um porgrama que tenha uma função fatrorial() que receba dois parametros: o priemiro que indique o numero a calcular e o outro chamado show, que sera um valor lógico (opcional) indicando se sera mostardo ou não na tela o processo de calculo fatorial (por padrao é falso). Definindo uma docstring

def fatorial(num, show=False):
    """função fatorial

    Args:
        num (int): numero a ser calculado o fatorial
        show (bool, optional): Se verdadeiro mostra a equação fatorial

    Returns:
        f: o fatorial de num 
    """
    fat = 1
    
    for c in range (num, 0, -1):
        if show:
            print(c, end=' ')
            if c> 1:
                print('x', end=' ')
            else:
                print('=', end=' ')

        fat *= c
    return fat
    
print(fatorial(9, show=True))


