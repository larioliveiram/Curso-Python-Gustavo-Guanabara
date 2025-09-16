# The National Swimming Confederation needs a program that reads an athlete's year of birth and displays their category according to age:
# Up to 9 years: MIRIM
# Up to 14 years: INFANTIL
# Up to 19 years: JUNIOR
# Up to 25 years: SENIOR

from datetime import date
anonasc = int(input('Em que ano você nasceu?'))
anoatual = date.today().year
if anoatual - anonasc <= 9:
    print(f' Como você tem menos de 9 anos, você é da categoria MIRIM!')
elif 9 < (anoatual - anonasc) <= 14:
    print(f' Como você tem entre 10 e 14 anos, é da catergoria INFANTIL!')
elif 15 <= (anoatual - anonasc) <= 19:
    print(f' Como você tem entre 15 e 19 anos, é da categoria JÚNIOR!')
elif 20 <= (anoatual - anonasc) <= 25:
    print(f' Como você tem entre 20 e 25 anos, é da categoria SÊNIOR!') 
else:
    print(f' Como você tem mais de 25 anos, é da categoria MASTER!')
