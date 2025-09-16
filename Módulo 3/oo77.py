# Create a program that has a tuple with several words (do not use accents). After that, you should display the vowels contained in each word. 

palavras = ('aprende', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiou'
for palavra in palavras:
    vogaispalavra = set(letra for letra in palavra if letra in vogais)
    print (f' A palavra {palavra.upper()} tem as {vogaispalavra} vogais.')