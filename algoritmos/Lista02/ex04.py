permutacao = input()
lista_permut = [x for x in permutacao]
ordem = 'abcdefghijklmnopqrstuvwxyz'
lista_ordem = [y for y in ordem]
segredo = input()
lista_segredo = [z for z in segredo]
lista_frase = []

for j in range(len(lista_segredo)):
    for i in range(0,26):
        if lista_segredo[j] == lista_permut[i]:
            lista_frase.append(lista_ordem[i])
            
        
frase = "".join(lista_frase)


print(frase)
