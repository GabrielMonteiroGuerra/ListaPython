print('Calculadora de IMC')
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso/(altura*altura)

if (imc >=18.5 and imc <= 24.9):
    print('Peso normal')
    
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso')
     
elif imc >= 30 and imc <= 39.9:
    print('Obesidade')
       
else:
    print('Obesidade grave')