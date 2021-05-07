#Conjectura de collatz

numero = 22
print(numero)
collatz = [numero]

while numero != 1:
  if numero %2 == 0 :
    print("par")
    numero/=2
  else:
    print("impar")
    numero=(numero*3)+1
  collatz.append(numero)
  print(numero)

print(collatz)
print(f'passos: {len(collatz)-2}')
print(f'maior num: {int(max(collatz))}')
