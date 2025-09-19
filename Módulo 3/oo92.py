# Create a program that reads a person’s name, year of birth (record the age in the dictionary), and work permit (0 if none), and registers them in a dictionary. If the work permit is not zero, the dictionary should also receive the year of hiring and the salary. Calculate and add, in addition to the age, at what age the person will retire (after 35 years of contribution).
from datetime import date

cadastro = {}
cadastro ['nome'] = str(input('Qual o seu nome? ')).strip().capitalize()
anonasc = int(input('Em qual ano você nasceu? '))
cadastro ['idade'] = date.today().year - anonasc
cadastro ['carteira'] = int(input('Qual o número da sua carteira de trabalho? [0 caso não tenha]'))

if cadastro['carteira'] != 0:
    anocontrato = int(input('Em qual ano você começou a trabalhar?'))
    cadastro ['salário'] = float(input(' Qual o seu salário atual? '))
    cadastro ['idadeaposentadoria'] = (anocontrato + 35) - anonasc
      
print(cadastro)
