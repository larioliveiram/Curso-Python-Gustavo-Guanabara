# Write a program that reads the width and height of a wall in meters, calculates its area, and the amount of paint needed to cover it, knowing that each liter of paint covers 2 m².

a = float (input('Qual a altura da perede?'))
l = float (input('Agora me conte qual a largura da parede?'))
print (f'Certo, então temos {a*l:.0f} m² e para pintá-los são necessários {(a*l)/2:.1f} litros de tinta')