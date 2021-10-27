print('Mostrar maior número')

numeros = [];

numeros.append(int(input('Digite o primeiro número: ')))
numeros.append(int(input('Digite o segundo número: ')))
numeros.append(int(input('Digite o terceiro número: ')))

if (numeros[0]>numeros[1] and numeros[0]>numeros[2]):
    print('Maior número: ',numeros[0])
    
elif (numeros[1]>numeros[0] and numeros[1]>numeros[2]):
    print('Maior número: ',numeros[1])
    
else:
    print('Maior número: ',numeros[2])    