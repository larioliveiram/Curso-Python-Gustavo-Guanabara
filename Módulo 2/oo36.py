# Write a program to approve a bank loan for the purchase of a house. The program will ask for the house price, the buyer's salary, and the number of years they will take to pay. The monthly installment cannot exceed 30% of the salary, otherwise the loan will be denied.

print('Bem vindo ao LM empréstimos bancários ')
casa = float (input('Qual o valor da casa dos sonhos? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar?'))
mensalidade = casa/(anos*12)
if mensalidade > salario*0.3:
    print(f'Empréstimo negado! A mensalidade de R${mensalidade:.2f} é maior que 30% do seu salário de R${salario:.2f}')
else:
    print(f'Empréstimo APROVADO! A mensalidade será de R${mensalidade:.2f} por mês durante {anos} anos')