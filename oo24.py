# Create a program that reads the name of a city and tells whether or not it starts with the name "Santo"

cidade = input ('Digite o nome da cidade em que nasceu?').strip().capitalize()
resposta = cidade[:5] == 'Santo'
print (f' A sua cidade em santo? {resposta}')
