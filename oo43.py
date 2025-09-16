# Develop a logic that reads a person's weight and height, calculates their BMI, and displays their status according to the table below:
# Below 18.5: Underweight
# Between 18.5 and 25: Ideal weight
# Between 25 and 30: Overweight
# Between 30 and 40: Obesity
# Above 40: Morbid obesity 

peso = float(input('Qual o seu peso em quilos?'))
altura = float(input('Qual a sua altura em metros?'))
IMC = (peso/(altura*altura))
pesoideal = 18.5 * (altura * altura)
pesoideal2 = 25 * (altura * altura)
if IMC < 18.5:
    print(f' Você está abaixo do peso, seu IMC é {IMC:.1f}. Seria ideal ganhar {pesoideal - peso:.0f}kg para atingir o IMC ideal de 18.5')
elif 18.5 <= IMC <= 25:
    print(f' Você está no peso ideal, seu IMC é {IMC:.1f}. Continue assim!')
elif 25 < IMC <30:
    print(f' Você está com sobrepeso, seu IMC é {IMC:.1f}. Seria ideal perder {peso - pesoideal2:.0f}kg para atingir o IMC ideal de 25')
elif 30 <= IMC <40:
    print(f' Você está com obesidade, seu IMC é {IMC:.1f}. Seria ideal perder {peso - pesoideal2:.0f}kg para atingir o IMC ideal de 25')
else: 
    print(f' Você está com obesidade mórbida, seu IMC é {IMC:.1f}. Seria ideal perder {peso - pesoideal2:.0f}kg para atingir o IMC ideal de 25')