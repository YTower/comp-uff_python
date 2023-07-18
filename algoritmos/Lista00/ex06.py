from functools import cmp_to_key

def cmp_medalha(p1, p2):
    if int(p1[1]) > int(p2[1]):
        return -1
    elif int(p1[1]) < int(p2[1]):
        return 1
    elif int(p1[2]) > int(p2[2]):
        return -1
    elif int(p1[2]) < int(p2[2]):
        return 1
    elif int(p1[3]) > int(p2[3]):
        return -1
    elif int(p1[2]) < int(p2[2]):
        return 1
    elif p1[0] < p2[0]:
        return -1
    elif p1[0] > p2[0]:
        return 1
    else:
        return 1

tabela = []
N = int(input())

for i in range(N):
    pais = input().split()
    tabela.append(pais)

tabela.sort(key = cmp_to_key(cmp_medalha))
for i in range(N):
    print(tabela[i][0], end=" ")
    print(tabela[i][1], end=" ")
    print(tabela[i][2], end=" ")
    print(tabela[i][3])
    