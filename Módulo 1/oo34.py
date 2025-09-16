# Write a program that asks for an employee's salary and calculates the amount of their raise. For salaries above R$1,250.00, calculate a 10% raise. For salaries equal to or below this amount, the raise is 15%.

salario = float(input('Qual o seu salário?'))
if salario>1250.00:
    print(f'Você receberá um aumento salarial de 10%, sendo assim, seu novo salário será de R$ {salario*1.10:.2f} reais')
else:
    print(f'Você receberá um aumento salarial de 15%, sendo assim, seu novo salário será de R$ {salario*1.15:.2f} reais')