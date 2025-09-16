# Create a program that calculates the amount to be paid for a product, considering its regular price and the payment method:
# Cash/cheque payment: 10% discount
# Card payment in full: 5% discount
# Up to 2 installments on the card: regular price
# 3 or more installments on the card: 20% interest

preço = float(input('Qual o preço do produto? R$'))
pag = int(input('Escolha a forma de pagamento:\n 1 - À vista dinheiro/cheque\n 2 - À vista no cartão\n 3 - Em até 2x no cartão\n 4 - Em 3x ou mais no cartão'))
if pag == 1:
    print(f'O valor do produto com 10% de desconto é de R${preço*0.9:.2f}')
elif pag == 2:
    print(f' O valor do produto com 5% de desconto é de R${preço*0.95:.2f}')
elif pag == 3:
    print(f'Serão 2 parcelas de R${preço/2:.2f} sem juros')
elif pag == 4:
    print(f' O valor final do produto será de R${preço*1.2:.2f}.')
    parcelas = int(input('Em quantas parcelas deseja fazer?'))
    print(f'Cada parcela ficará R${(preço*1.2)/parcelas:.2f}')
else:
    print('Opção inválida! Tente novamente.')