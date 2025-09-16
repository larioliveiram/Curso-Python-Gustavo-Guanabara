# Write a program that reads a car's speed. If it exceeds 80 km/h, display a message saying the driver has been fined. The fine will cost R$7 for each kilometer over the limit.

vcarro = float (input('Qual a velocidade do carro?'))
if vcarro >80:
    print(f'Você ultrapassou o limite de velocidade, você deve pagar uma multa de R$ {(vcarro-80)*7:.2f} reais)')
else:
    print('Você é um motorista consciente, continue assim!')