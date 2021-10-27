print('Velocidade de download')
arquivo = float(input('Digite o tamanho do arquivo em MB: '))
internet = float(input('Digite a velocidade da internet em MBs: '))

tempo = arquivo/(internet/8)

print('O tempo para a realização do download é: ',tempo,'segundos')