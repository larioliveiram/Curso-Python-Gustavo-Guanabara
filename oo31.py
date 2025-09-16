# Develop a program that asks for the distance of a trip in km. Calculate the ticket price, charging R$0.50 per km for trips up to 200 km and R$0.45 for longer trips.

kmviagem = float (input('Quantos km até o seu destino?'))
if kmviagem <= 200:
    print (f' Nesse caso, é cobrado R$0,50 por km rodado. Sua passagem custará R$ {kmviagem*0.50:.2f} ')
else:
    print (f'Nesse caso, é cobrado R$0,45 por km rodado. Sua passagem custará R$ {kmviagem*0.45:.2f} ')

# A simplified way to write the code above would be:
preço = kmviagem*0.50 if kmviagem <=200 else kmviagem*0.45
print (f'Sua passagem custará R$ {preço:.2f} ')