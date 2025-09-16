# Write a program that reads a value in meters and displays it converted into centimeters and millimeters.

m = float (input('Qual o seu tamanho?'))
print(f'Isso quer dizer que você tem {m*100:.0f} centimetros e {m*1000:.0f} milimetros')