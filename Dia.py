print('Bom dia, boa tarde e boa noite')

turno = str(input('Digite o seu turno, M-matutino, V-vespertino ou N-Noturno: '))

while (turno != 'M' and turno != 'V' and turno != 'N'):
 turno = str(input('Digite o seu turno, M-matutino, V-vespertino ou N-Noturno: '))
 
if (turno == 'M'):
    print('Bom dia!')
    
if  (turno == 'V'):
    print('Boa tarde!')
    
if  (turno == 'N'):
    print('Boa noite!')
    