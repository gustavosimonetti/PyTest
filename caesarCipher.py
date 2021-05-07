    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    #dados = "teste"
    dados = "ôróôr"
    chave=13
    #modo='enc' #enc/dec = encripta/decripta
    modo='dec'
  
    strCifrada = ''
    for c in dados:
        index = alfabeto.find(c)
        if index == -1:
            strCifrada += c
        else:            
            if modo == 'enc':
              new_index = index + chave 
            else:
              new_index = index - chave

            new_index = new_index % len(alfabeto)
            strCifrada += alfabeto[new_index:new_index+1]
    
    print(strCifrada)
