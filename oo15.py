# Write a program that asks for the number of kilometers driven by a rented car and the number of days it was rented. Calculate the total price, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.

km = float (input('Quantos km você rodou com o carro?'))
dias = int (input('Por quantos dias você alugou o carro?'))
print (f'O total a ser pago é R$ {0.15*km + 60*dias:.2f}')