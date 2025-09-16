# Write a program that reads a young person's year of birth and informs, based on their age:
# -If they still need to enlist for military service
# -If it is time to enlist
# -If the enlistment period has already passed
# Your program should also display how much time is left or how much time has passed since the deadline.


from datetime import date
anonasc = int(input('Em que ano você nasceu?'))
anoatual =  date.today().year
if (anoatual - anonasc) <18:
    print(f' Você ainda não tem idade para se alistar, faltam {18 - (anoatual-anonasc)} anos') 
elif (anoatual - anonasc) == 18:
    print (f' Você já tem {anoatual-anonasc} anos, é hora de se alistar!')
else:
    print(f' Você já passou do tempo de se aliastar faz {(anoatual-anonasc) - 18}')                            