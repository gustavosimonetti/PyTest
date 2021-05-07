'''
Calculo do digito verificador do CPF
'''
#cpf="529.982.247-25" teste para validar
cpf="529.982.247"
a = cpf.split('.')[0]+cpf.split('.')[1]+cpf.split('.')[2]
print(a)

#calculo primeiro Digito
multiplicador=10
soma=0

for ch in a:
  print(f'multiplicador{multiplicador}')
  soma+=int(ch)*multiplicador
  print(f'soma {soma}')
  multiplicador-=1
if ((soma*10)%11) == 10:
  digito1 = 0
else:
  digito1 = (soma*10)%11

print(digito1)

#calculo segundo Digito
multiplicador=11
soma=0
for ch in a:
  print(f'multiplicador{multiplicador}')
  soma+=int(ch)*multiplicador
  print(f'soma {soma}')
  multiplicador-=1
soma+=dig1*multiplicador

#
if ((soma*10)%11) == 10:
  digito2 = 0
else:
  digito2 = (soma*10)%11
    
print(digito2)


#Digito verificador final 
DV=str(digito1) + str(digito2)
