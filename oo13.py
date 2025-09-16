# Write an algorithm that reads an employee's salary and displays their new salary with a 15% increase.

s = float (input('Qual o seu salário?'))
print(f'Hoje você foi promovido! Passará a ganhar 15% a mais, ou seja, {s*1.15:.2f}')
print(f'É possivel também fazer a conta da seguinte maneira {s+(s*15/100):.2f}')