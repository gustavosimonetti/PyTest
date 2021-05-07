    chave = 3
    mensagem = "Em noite de lua cheia, enquanto o Canguçu esturra, o Guatipuru sobe na Carapanaúba?"
    nA = ord('A')
    nZ = ord('Z')
    na = ord('a')
    nz = ord('z')
    for caracter in mensagem:
        ind = ord(caracter)
        if nA <= ind <= nZ:
            nova_letra = chr((ind + chave)%(nZ+1) + ((ind + chave)//(nZ+1))*nA)
            # substituir na mensagem a letra pela nova_letra
            cifrada = cifrada + nova_letra
        elif ind in range(na, nz+1):
            nova_letra = chr((ind + chave)%(nZ+1) + ((ind + chave)//(nZ+1))*nA)
            cifrada = cifrada + nova_letra
        else:
            cifrada = cifrada + caracter
    print("Original: ", mensagem)
    print("Cifrada: ", cifrada)
