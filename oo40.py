# Create a program that reads two grades of a student and calculates their average, displaying a message at the end according to the achieved average:
# Average below 5.0: FAILED
# Average between 5.0 and 6.9: RECOVERY
# Average 7.0 or higher: PASSED

nota1 = float(input('Digite a nota da priemira prova:'))
nota2 = float(input('Digiete a nota da segunda prova:'))
media = (nota1 + nota2)/2
if media <5:
    print(f'Sua média é {media:.1f}, você foi REPROVADO!')
elif 5.0 <= media and media <= 6.9:
    print(f' Sua média é {media:.1f}, você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Sua média é {media:.1f}, você foi APROVADO!')
