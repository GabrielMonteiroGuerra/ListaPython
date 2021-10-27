print('Programa calculo do pescador')
peso = int(input('Digite o peso de peixes: '))
#Sempre que o peso for > 50 deve pagar R$ 4,00 a cada quilo excedente (apensar números inteiros)
excesso = peso - 50
multa = excesso * 4
print('A multa a pagar é: R$',multa,'reais')