text = "Python Rlz!"
s = 4
result = ""
mode='enc' # modo enc/dec - encrypt/decrypt

if mode == 'dec':
 s *= -1
 
# traverse text
for i in range(len(text)):
  if text[i].isalpha():
    result += text[i]
    continue
  
  char = text[i]
 
  # Encrypt uppercase characters
  if (char.isupper()):
    result += chr((ord(char) + s-65) % 26 + 65)
 
  # Encrypt lowercase characters
  else:
    result += chr((ord(char) + s - 97) % 26 + 97)
 
print(f'result {result}')
