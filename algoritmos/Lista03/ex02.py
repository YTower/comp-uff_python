N= int(input())
lista_de_predios = list(map(int, input().split()))

distancia = 0

for i in range(1, N):
    nova_distancia = lista_de_predios[0] + i + lista_de_predios[i]
    if nova_distancia > distancia:
        distancia = nova_distancia
        ind = i

distancia_maxima = 0
for i in range(N):
    if i != ind:
        nova_distancia = lista_de_predios[ind] + lista_de_predios[i]+(ind - i)
        distancia_maxima = max(distancia_maxima, nova_distancia)
print(distancia_maxima)
